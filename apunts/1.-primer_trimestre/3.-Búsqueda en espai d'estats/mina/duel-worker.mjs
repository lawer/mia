const CDN = "https://cdn.jsdelivr.net/pyodide/v314.0.8/full/";
let python;

async function text(path) {
  const response = await fetch(new URL(path, import.meta.url));
  if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
  return response.text();
}

self.onmessage = async ({ data }) => {
  try {
    if (data.type === "start") {
      const [{ loadPyodide }, motor, model] = await Promise.all([
        import(`${CDN}pyodide.mjs`),
        text("mina.py"),
        text("bot_model.py"),
      ]);
      python = await loadPyodide({ indexURL: CDN });
      python.FS.writeFile("mina.py", motor);
      for (const [index, source] of data.bots.entries()) {
        python.FS.writeFile(`jugador_${index}.py`, source ?? model);
      }
      python.globals.set("llavor_text", data.seed);
      python.runPython(`
import json
from runpy import run_path
from mina import dibuixa_emojis, genera_mina, torns_partida

def bot(index):
    decideix = run_path(f"jugador_{index}.py").get("decideix")
    if not callable(decideix):
        raise ValueError(f"Bot {index + 1}: decideix(vista)")
    def valida(vista):
        accio = decideix(vista)
        if accio not in ("N", "S", "E", "O", "ESPERA"):
            raise ValueError(f"Bot {index + 1}: {accio!r}")
        return accio
    return valida

mina = genera_mina(int(llavor_text))
torns = torns_partida(mina, (bot(0), bot(1)))

def seguent():
    try:
        torn, robots, disponible = next(torns)
    except StopIteration as fi:
        return json.dumps({"type": "end", "winner": fi.value})
    return json.dumps({
        "type": "frame", "turn": torn,
        "board": dibuixa_emojis(mina, robots, disponible),
        "robots": [{"energy": r.energia, "delay": r.retard} for r in robots],
    })
`);
    }
    self.postMessage(JSON.parse(python.runPython("seguent()")));
  } catch (error) {
    self.postMessage({ type: "error", message: error.message });
  }
};
