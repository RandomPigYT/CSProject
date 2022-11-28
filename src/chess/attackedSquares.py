from chess import globals as g
from chess import generateMoves as gm


def getCriticalLines(pos, colour):
    # N, S, E, W, NE, NW, SE, SW
    directions = [8, -8, 1, -1, 9, 7, -7, -9]

    criticalLines = []

    for i in range(len(directions)):
        temp = pos

        for j in range(g.distToEdge[pos][i]):
            pass


def attackedSquares(colour) -> list:
    pieces = []

    g.attacked = []

    if colour == g.Piece.white:
        pieces = g.whitePieceLocations

    else:
        pieces = g.blackPieceLocations

    for i in pieces:
        if g.board[i] & 0b00111 == g.Piece.Pawn:
            g.attacked.extend(gm.pawnAttacks((g.board[i], i)))
            continue

        elif g.board[i] & 0b00111 != g.Piece.King:
            g.attacked.extend(gm.generateMoves((g.board[i], i)))
