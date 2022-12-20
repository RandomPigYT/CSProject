from chess import globals as g
from chess import util as u
from chess import check

# 0 = king-side castling
# 1 = queen-side castling
castleSquares = {
    g.Piece.white: [[6, 7], [0, 1, 2]],
    g.Piece.black: [[62, 63], [56, 57, 58]],
}

# Starting position of the kings
kingPos = {g.Piece.white: 4, g.Piece.black: 60}

# Starting position of the rooks
# indices:
#   0 = king-side rook
#   1 = queen-side rook
rookPos = {g.Piece.white: [7, 0], g.Piece.black: [63, 56]}

# Squares that, if attacked, will prevent castling
safeSquares = {g.Piece.white: [[5, 6], [2, 3]], g.Piece.black: [[61, 62], [58, 59]]}
emptySquares = {
    g.Piece.white: [[5, 6], [1, 2, 3]],
    g.Piece.black: [[61, 62], [57, 58, 59]],
}


class Castle:
    colourOffset = {8: 2, 16: 0}

    # 0: kingSide
    # 1: queenSide
    sideOffset = [1, 0]


def side(endPos, colour, castleSquares):
    for i in range(len(castleSquares[colour])):
        if endPos in castleSquares[colour][i]:
            return i
    else:
        return -1


def castle(endPos, colour):

    castleSide = side(endPos, colour, castleSquares)

    g.board[endPos] = 0

    g.board[kingPos[colour]] = 0
    g.board[rookPos[colour][castleSide]] = 0

    if castleSide == 0:
        g.board[kingPos[colour] + 1] = g.Piece.Rook | colour
        g.board[kingPos[colour] + 2] = g.Piece.King | colour

    else:
        g.board[kingPos[colour] - 1] = g.Piece.Rook | colour
        g.board[kingPos[colour] - 2] = g.Piece.King | colour


def canCastle(endPos, colour):

    castleSide = side(endPos, colour, castleSquares)

    if (
        not g.canCastle
        & (0b1 << Castle.colourOffset[colour]) << Castle.sideOffset[castleSide]
    ):
        return False

    for i in safeSquares[colour][castleSide]:
        if i in g.attacked:
            return False

    for i in emptySquares[colour][castleSide]:
        if g.board[i] != 0:
            return False

    if check.isCheck():
        return False

    return True


def isCastling(endPos, colour) -> bool:
    for i in castleSquares[colour]:
        if endPos in i:
            return True and g.heldPiece[0] & g.pieceMask == g.Piece.King and canCastle(endPos, colour)

    return False
