from chess import globals as g
from chess import generateMoves as gm
from chess import pieceLocations as pl
from chess import attackedSquares as a


def makeMove(startSquare, endSquare) -> bool:
    def isSameColour(b):  # {
        if g.heldPiece[0] & g.colourMask == g.board[b] & g.colourMask:
            return True

        return False

    # }

    moves = gm.generateMoves(g.heldPiece)

    if (
        g.board[endSquare] != g.Piece.empty
        and isSameColour(endSquare)
        or endSquare == -1
        or (g.heldPiece[0] & g.colourMask) != g.turn
        or endSquare not in moves
    ):

        g.board[g.heldPiece[1]] = g.heldPiece[0]
        g.heldPiece = ()

        return False

    else:

        g.board[endSquare] = g.heldPiece[0]
        g.heldPiece = ()

        # Keep track of pieces
        pl.pieceLocations()

        return True
