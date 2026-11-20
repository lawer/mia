"""Motor de La cursa de la mina. Python 3.10+, sense dependències."""
from collections import deque
from dataclasses import dataclass, replace
from random import Random

PASSOS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
COSTOS = {".": 1, ":": 3}
RETARD = 2


@dataclass(frozen=True)
class Mina:
    mapa: tuple[str, ...]
    eixides: tuple[tuple[int, int], tuple[int, int]]
    tresor: tuple[int, int]
    bomba: tuple[int, int]
    bateria: int


@dataclass(frozen=True)
class Robot:
    posicio: tuple[int, int]
    energia: int
    retard: int = 0


@dataclass(frozen=True)
class Vista:
    mina: Mina
    jo: Robot
    rival: Robot
    bomba_disponible: bool
    torn: int


def successors(mina, posicio, energia):
    """Genera (accio, posicio nova, energia restant) per a cada moviment legal."""
    fila, columna = posicio
    for accio, (df, dc) in PASSOS.items():
        f, c = fila + df, columna + dc
        if 0 <= f < len(mina.mapa) and 0 <= c < len(mina.mapa[f]):
            cost = COSTOS.get(mina.mapa[f][c])
            if cost is not None and energia >= cost:
                yield accio, (f, c), energia - cost


def _abast(mina, origen):
    """Posicions assolibles des de l'origen amb la bateria inicial."""
    cua = deque([(origen, mina.bateria)])
    millor = {origen: mina.bateria}
    while cua:
        posicio, energia = cua.popleft()
        for _, desti, restant in successors(mina, posicio, energia):
            if restant > millor.get(desti, -1):
                millor[desti] = restant
                cua.append((desti, restant))
    return millor


def genera_mina(llavor, files=9, columnes=13):
    """Genera una mina jugable a partir de la llavor i les dimensions."""
    if not 5 <= files <= 21 or not 5 <= columnes <= 25:
        raise ValueError("Calen 5–21 files i 5–25 columnes")
    rng = Random(llavor)
    eixides = ((1, 1), (1, columnes - 2))
    tresor = (files - 2, columnes // 2)
    distancia_base = files - 3 + columnes // 2 - 1
    for intent in range(100):
        mapa = tuple(
            "".join(
                "." if (f, c) in (*eixides, tresor)
                else rng.choices("#.:", (23, 55, 22))[0]
                for c in range(columnes)
            )
            for f in range(files)
        )
        if intent == 99:
            # Garanteix una galeria fins al tresor si la resta de mapes fallen.
            graella = [list(fila) for fila in mapa]
            for c in range(1, columnes - 1):
                graella[1][c] = "."
            for f in range(1, files - 1):
                graella[f][tresor[1]] = "."
            mapa = tuple("".join(fila) for fila in graella)
        bateria = max(7, rng.randint(19, 24) + 2 * (distancia_base - 11))
        mina = Mina(mapa, eixides, tresor, tresor, bateria)
        abasts = [_abast(mina, eixida) for eixida in eixides]
        if any(tresor not in abast for abast in abasts):
            continue
        candidats = []
        fins_tresor = _abast(mina, tresor)
        for posicio in sorted(abasts[0].keys() & abasts[1].keys() & fins_tresor.keys()):
            if posicio in (*eixides, tresor):
                continue
            f, c = posicio
            # En invertir el camí, canvia el cost de la primera i l'última casella.
            cost_fins_tresor = bateria - fins_tresor[posicio] + 1 - COSTOS[mapa[f][c]]
            if all(abast[posicio] >= cost_fins_tresor for abast in abasts):
                candidats.append(posicio)
        if candidats:
            return replace(mina, bomba=rng.choice(candidats))


def torns_partida(mina, bots, maxim_torns=60):
    """Produeix un estat per torn i retorna el guanyador en acabar."""
    robots = tuple(Robot(posicio, mina.bateria) for posicio in mina.eixides)
    disponible = True
    yield 0, robots, disponible
    for torn in range(1, maxim_torns + 1):
        nous = list(robots)
        for i, bot in enumerate(bots):
            robot = robots[i]
            if robot.retard:
                nous[i] = replace(robot, retard=robot.retard - 1)
                continue
            accio = bot(Vista(mina, robot, robots[1 - i], disponible, torn))
            for moviment, posicio, energia in successors(mina, robot.posicio, robot.energia):
                if accio == moviment:
                    nous[i] = Robot(posicio, energia)
                    break
        if disponible:
            primers = [i for i, robot in enumerate(nous) if robot.posicio == mina.bomba]
            if primers:
                disponible = False
                if len(primers) == 1:
                    rival = 1 - primers[0]
                    nous[rival] = replace(nous[rival], retard=RETARD)
        robots = tuple(nous)
        yield torn, robots, disponible
        arribades = [i for i, robot in enumerate(robots) if robot.posicio == mina.tresor]
        if arribades:
            return arribades[0] if len(arribades) == 1 else None
    return None



def juga(mina, bots, maxim_torns=60, *, en_torn=None):
    """Retorna (guanyador, historial). Guanyador és 0, 1 o None si hi ha empat."""
    torns = torns_partida(mina, bots, maxim_torns)
    historial = []
    while True:
        try:
            torn, robots, disponible = next(torns)
        except StopIteration as fi:
            return fi.value, historial
        historial.append((robots, disponible))
        if en_torn is not None:
            en_torn(torn, robots, disponible)


def dibuixa(mina, robots, disponible):
    mapa = [list(fila) for fila in mina.mapa]
    for posicio, simbol in ((mina.tresor, "T"), (mina.bomba, "B")):
        if simbol != "B" or disponible:
            f, c = posicio
            mapa[f][c] = simbol
    for i, robot in enumerate(robots):
        f, c = robot.posicio
        mapa[f][c] = "X" if mapa[f][c] == "1" else str(i + 1)
    return "\n".join(" ".join(fila) for fila in mapa)


_ICONES = {
    "#": "🧱", ".": "⬛", ":": "🟫", "T": "💎", "B": "💣",
    "1": "🔵", "2": "🟠", "X": "🟣",
}


def dibuixa_emojis(mina, robots, disponible):
    """Mostra el tauler amb els colors dels robots i del terreny."""
    tauler = dibuixa(mina, robots, disponible)
    return "\n".join(
        " ".join(_ICONES[simbol] for simbol in fila.split())
        for fila in tauler.splitlines()
    )
