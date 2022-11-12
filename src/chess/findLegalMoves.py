from chess import globals as g
from chess import generateMoves as gm


def isLegalMove(startSquare, endSquare) -> bool:

    isSameColour = (
        lambda b: True if g.heldPiece[0] & 0b11000 == g.board[b] & 0b11000 else False
    )

    if g.board[endSquare] != g.Piece.empty and isSameColour(endSquare):
        return False

    if endSquare in gm.generateMoves(g.heldPiece):
        return True
