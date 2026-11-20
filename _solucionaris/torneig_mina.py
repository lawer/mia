"""Torneig local per al professorat, en Linux o macOS.

Des de l'arrel del repositori:
PYTHONPATH="apunts/1.-primer_trimestre/3.-Búsqueda en espai d'estats/mina" python _solucionaris/torneig_mina.py lliuraments --mapes 5

Afig --directe per veure totes les partides o --directe anna joan per
projectar només els enfrontaments entre dos àlies. Amb --interval pots
canviar la pausa entre torns (per defecte, 0.35 segons).

Posa un .py per alumne a lliuraments, amb el seu àlies com a nom de fitxer.
Tanca els lliuraments abans de generar les mines. Guarda la llavor del
resultat per poder repetir-lo amb --llavor. Les partides duren 60 torns
com a màxim. Cada victòria val 3 punts i cada empat, 1.

Executa únicament fitxers revisats. El límit per decisió no aïlla el codi.
"""
import argparse
from collections import Counter
from dataclasses import replace
from itertools import combinations
from math import isfinite
from pathlib import Path
from random import Random
from runpy import run_path
from secrets import randbits
from signal import ITIMER_REAL, SIGALRM, setitimer, signal
import sys
from time import sleep
from contextlib import redirect_stdout

from mina import dibuixa_emojis, genera_mina, juga


def _temps_esgotat(_senyal, _marc):
    raise TimeoutError("temps esgotat")


def amb_limit(funcio, *args):
    setitimer(ITIMER_REAL, 0.15)
    try:
        with redirect_stdout(sys.stderr):
            return funcio(*args)
    finally:
        setitimer(ITIMER_REAL, 0)


def carrega(cami):
    decideix = amb_limit(run_path, str(cami)).get("decideix")
    if not callable(decideix):
        raise ValueError("falta la funció decideix(vista)")
    return decideix


def duel(mina, fitxers, *, en_torn=None):
    errors = {}

    def prepara(i, fitxer):
        try:
            decideix = carrega(fitxer)
        except Exception as error:
            errors[i] = (0, type(error).__name__)
            return lambda vista: "ESPERA"

        def bot(vista):
            if i not in errors:
                try:
                    accio = amb_limit(decideix, vista)
                    if not isinstance(accio, str) or accio not in ("N", "S", "E", "O", "ESPERA"):
                        raise ValueError("acció desconeguda")
                    return accio
                except Exception as error:
                    errors[i] = (vista.torn, type(error).__name__)
            return "ESPERA"
        return bot

    bots = tuple(prepara(i, fitxer) for i, fitxer in enumerate(fitxers))
    guanyador, historial = juga(mina, bots, en_torn=en_torn)
    if errors:
        primer_torn = min(torn for torn, _ in errors.values())
        primers = [i for i, (torn, _) in errors.items() if torn == primer_torn]
        guanyador = 1 - primers[0] if len(primers) == 1 else None
    return guanyador, len(historial) - 1, errors


def vista_en_directe(mina, noms, titol, interval):
    def mostra(torn, robots, disponible):
        if sys.stdout.isatty():
            print("\033[2J\033[H", end="")
        print(f"{titol} · Torn {torn} · {' vs '.join(noms)}")
        print(dibuixa_emojis(mina, robots, disponible))
        for icona, nom, robot in zip(("🔵", "🟠"), noms, robots):
            print(f"{icona} {nom} · 🔋 {robot.energia} · ⏳ {robot.retard}")
        sys.stdout.flush()
        sleep(interval)
    return mostra


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("lliuraments", type=Path, help="Directori amb un fitxer .py per alumne")
    parser.add_argument("--mapes", type=int, default=5)
    parser.add_argument("--llavor", type=int, help="Permet repetir un torneig anterior")
    parser.add_argument("--directe", nargs="*", metavar="ÀLIES",
                        help="Projecta totes les partides o indica els dos bots a mostrar")
    parser.add_argument("--interval", type=float, default=0.35,
                        help="Pausa en segons després de cada torn visible")
    args = parser.parse_args()
    fitxers = sorted(args.lliuraments.glob("*.py"))
    if len(fitxers) < 2 or args.mapes < 1:
        parser.error("Calen almenys dos bots i un mapa")
    if not isfinite(args.interval) or args.interval < 0:
        parser.error("L'interval ha de ser un nombre finit i no negatiu")
    if args.directe and (len(set(args.directe)) != 2 or len(args.directe) != 2
                         or not set(args.directe) <= {p.stem for p in fitxers}):
        parser.error("--directe accepta dos àlies diferents de bots del torneig")
    signal(SIGALRM, _temps_esgotat)
    llavor = randbits(64) if args.llavor is None else args.llavor
    rng = Random(llavor)
    mines = [genera_mina(rng.getrandbits(64)) for _ in range(args.mapes)]
    punts = Counter({p.stem: 0 for p in fitxers})
    victories = punts.copy()
    empats = punts.copy()
    for parella in combinations(fitxers, 2):
        noms = [p.stem for p in parella]
        for numero, mina in enumerate(mines, 1):
            for volta, eixides in enumerate((mina.eixides, mina.eixides[::-1]), 1):
                tauler = replace(mina, eixides=eixides)
                mostra = None
                if args.directe == [] or (args.directe and set(args.directe) == set(noms)):
                    mostra = vista_en_directe(tauler, noms, f"Mina {numero}.{volta}", args.interval)
                guanyador, torns, errors = duel(tauler, parella, en_torn=mostra)
                if guanyador is None:
                    punts.update(noms)
                    empats.update(noms)
                else:
                    nom = noms[guanyador]
                    punts[nom] += 3
                    victories[nom] += 1
                resultat = "empat" if guanyador is None else noms[guanyador]
                print(f"Mina {numero}.{volta} | {' vs '.join(noms)} | {resultat} | {torns} torns")
                for i, (torn, error) in errors.items():
                    print(f"  {noms[i]} — torn {torn}: {error}")
    print("\nPosició  Punts  Victòries  Empats  Bot")
    rang = 0
    anterior = None
    for i, nom in enumerate(sorted(punts, key=lambda nom: (-punts[nom], -victories[nom], nom)), 1):
        clau = (punts[nom], victories[nom])
        if clau != anterior:
            rang = i
        print(f"{rang:>7} {punts[nom]:>6} {victories[nom]:>10} {empats[nom]:>7}  {nom}")
        anterior = clau
    print(f"\nLlavor del torneig: {llavor}")


if __name__ == "__main__":
    main()
