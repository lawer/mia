const game = document.querySelector("#mina-duel");
const form = game.querySelector("form");
const start = game.querySelector("[type=submit]");
const stop = game.querySelector("[data-stop]");
const status = game.querySelector("[role=status]");
const board = game.querySelector("pre");
const players = game.querySelector("[data-players]");
const seedField = form.elements.seed;
const labels = game.dataset;
let worker;
let timer;
let watchdog;

function finish(message) {
  clearTimeout(timer);
  clearTimeout(watchdog);
  worker?.terminate();
  worker = null;
  start.disabled = false;
  stop.disabled = true;
  status.textContent = message;
}

stop.addEventListener("click", () => finish(labels.stopped));
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (start.disabled) return;
  start.disabled = true;
  status.textContent = labels.loading;
  board.textContent = "";
  players.textContent = "";
  try {
    const files = ["blue", "orange"].map(name => form.elements[name].files[0]);
    const bots = await Promise.all(files.map(file => file ? file.text() : null));
    const names = files.map((file, i) => file?.name ?? `Bot ${i + 1}`);
    const seed = seedField.value.trim() || String(crypto.getRandomValues(new Uint32Array(1))[0]);
    seedField.value = seed;
    const interval = Number(form.elements.interval.value);
    const duel = new Worker(new URL("duel-worker.mjs", import.meta.url), { type: "module" });
    worker = duel;
    stop.disabled = false;
    watchdog = setTimeout(() => finish(labels.timeout), 45000);
    duel.onerror = () => finish(labels.runtimeError);
    duel.onmessage = ({ data }) => {
      if (worker !== duel) return;
      clearTimeout(watchdog);
      if (data.type === "error") {
        finish(`${labels.runtimeError} ${data.message}`);
      } else if (data.type === "end") {
        finish(data.winner === null ? labels.draw : `${labels.win} ${names[data.winner]}`);
      } else if (data.type === "frame") {
        board.textContent = data.board;
        status.textContent = `${labels.turn} ${data.turn}`;
        players.textContent = data.robots.map((robot, i) =>
          `${["🔵", "🟠"][i]} ${names[i]} · 🔋 ${robot.energy} · ⏳ ${robot.delay}`
        ).join("\n");
        timer = setTimeout(() => {
          watchdog = setTimeout(() => finish(labels.timeout), 3000);
          duel.postMessage({ type: "next" });
        }, interval);
      }
    };
    duel.postMessage({ type: "start", bots, seed });
  } catch (error) {
    finish(`${labels.runtimeError} ${error.message}`);
  }
});
