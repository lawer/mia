"""Copia aquest fitxer i implementa decideix amb la teua estratègia."""
from mina import successors


def decideix(vista):
    # Punt de partida: tria la casella més pròxima al tresor.
    fila, columna = vista.mina.tresor
    moviments = successors(vista.mina, vista.jo.posicio, vista.jo.energia)
    millor = min(
        moviments,
        key=lambda moviment: abs(moviment[1][0] - fila) + abs(moviment[1][1] - columna),
        default=None,
    )
    return millor[0] if millor else "ESPERA"
