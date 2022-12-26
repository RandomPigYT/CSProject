from chess import globals as g
from chess import generateMoves as gm
from chess import pieceLocations as pl
from chess import attackedSquares as a
from chess import util as u
from chess import castling
from chess import check


def disableCastling():
    if g.turn == g.Piece.white:
        g.canCastle &= 0b0011

    else:
        g.canCastle &= 0b1100


def makeMove(startSquare, endSquare) -> bool:

    if startSquare == endSquare:

        g.board[g.heldPiece[1]] = g.heldPiece[0]
        g.heldPiece = ()

        return False

    def isSameColour(b):  # {
        if g.heldPiece[0] & g.colourMask == g.board[b] & g.colourMask:
            return True

        return False

    # }

    moves = gm.generateMoves(g.heldPiece)

    isCastling = castling.isCastling(endSquare, g.turn)

    if not isCastling and (
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
    
        criticalLines = a.getCriticalLines(u.findKing(g.turn), g.turn)

        for i in criticalLines:

            if startSquare in i and endSquare not in i:
                g.board[g.heldPiece[1]] = g.heldPiece[0]
                g.heldPiece = ()

                return False

        if isCastling and castling.canCastle(endSquare, g.turn):

            castling.castle(endSquare, g.turn)
            g.heldPiece = ()

            disableCastling()

            pl.pieceLocations()
            a.attackedSquares(g.turn)

            return True

        elif isCastling and not castling.canCastle(endSquare, g.turn):
            g.board[g.heldPiece[1]] = g.heldPiece[0]
            g.heldPiece = ()

            return False

        if g.heldPiece[0] & g.pieceMask == g.Piece.King:
            disableCastling()
            
        # Disable castling
        if g.heldPiece[0] & g.pieceMask == g.Piece.Rook:
            g.canCastle &= ~(
                (0b1 << castling.Castle.colourOffset[g.turn])
                << castling.Castle.sideOffset[castling.side(startSquare, g.turn)]
            )
            print(bin(g.canCastle))

        if endSquare in castling.rookPos[g.turn ^ g.colourMask]:
            g.canCastle &= ~(
                (0b1 << castling.Castle.colourOffset[g.turn ^ g.colourMask])
                << castling.Castle.sideOffset[castling.side(endSquare, g.turn ^ 0b11000)]
            )
            print(bin(g.canCastle))


        boardCopy = check.makeTempMove(startSquare, endSquare)
        print("okay,",boardCopy == g.board)

        if check.isCheck():
            print("illegal")

            check.unmakeMove(boardCopy)

            g.board[g.heldPiece[1]] = g.heldPiece[0]
            g.heldPiece = ()

            return False


        g.board[endSquare] = g.heldPiece[0]
        g.heldPiece = ()

        # Keep track of pieces
        pl.pieceLocations()
        a.attackedSquares(g.turn)

        return True
