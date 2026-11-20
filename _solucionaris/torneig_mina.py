"""Torneig local per al professorat, en Linux o macOS.

Des de l'arrel del repositori:
PYTHONPATH="apunts/1.-primer_trimestre/3.-Búsqueda en espai d'estats/mina" python _solucionaris/torneig_mina.py lliuraments --mapes 5

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
from pathlib import Path
from random import Random
from runpy import run_path
from secrets import randbits
from signal import ITIMER_REAL, SIGALRM, setitimer, signal
import sys
from contextlib import redirect_stdout

from mina import genera_mina, juga


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


def duel(mina, fitxers):
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
    guanyador, historial = juga(mina, bots)
    if errors:
        primer_torn = min(torn for torn, _ in errors.values())
        primers = [i for i, (torn, _) in errors.items() if torn == primer_torn]
        guanyador = 1 - primers[0] if len(primers) == 1 else None
    return guanyador, len(historial) - 1, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lliuraments", type=Path, help="Directori amb un fitxer .py per alumne")
    parser.add_argument("--mapes", type=int, default=5)
    parser.add_argument("--llavor", type=int, help="Permet repetir un torneig anterior")
    args = parser.parse_args()
    fitxers = sorted(args.lliuraments.glob("*.py"))
    if len(fitxers) < 2 or args.mapes < 1:
        parser.error("Calen almenys dos bots i un mapa")
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
                guanyador, torns, errors = duel(replace(mina, eixides=eixides), parella)
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
