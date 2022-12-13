from chess import globals as g


def coordsToIndex(rank, file):
    return rank * 8 + file


def indexToCoords(index):
    return (index % 8, int(index / 8))


def findKing(colour):
    for i in range(len(g.board)):
        if (
            g.board[i] & g.pieceMask == g.Piece.King
            and g.board[i] & g.colourMask == colour
        ):
            return i

    return g.heldPiece[1]
