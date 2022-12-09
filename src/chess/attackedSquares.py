from chess import globals as g
from chess import generateMoves as gm
from chess import util as u


def getCriticalLines(kingPos, colour) -> list:
    # N, S, E, W, NE, NW, SE, SW
    directions = [8, -8, 1, -1, 9, 7, -7, -9]

    def lineAttacked(piece, dirIndex) -> bool:  # {
        if dirIndex < 4:
            if piece >= g.Piece.Rook:
                return True

        elif piece == g.Piece.Bishop or piece == g.Piece.Queen:
                return True

        return False

    # }

    criticalLines = []

    for i in range(len(directions)):
        numBarriers = 0
        isCritical = False

        line = []

        temp = kingPos
        for j in range(g.distToEdge[kingPos][i]):
            temp += directions[i]

            line.append(temp)

            if g.board[temp]:

                if g.board[temp] & g.colourMask != colour and not lineAttacked(g.board[temp] & g.pieceMask, i) and not isCritical:
                    break

                # If the enemy piece is attacking a line defended by only one
                # piece, the line is critical
                if (
                    lineAttacked(g.board[temp] & g.pieceMask, i)
                    and numBarriers == 1
                    and g.board[temp] & g.colourMask == colour ^ g.colourMask
                ):
                    isCritical = True

                elif g.board[temp] & g.colourMask == colour:
                    numBarriers += 1

            # Check if the currently held piece was defending the line
            elif len(g.heldPiece) and g.heldPiece[1] == temp:
                numBarriers += 1

        if isCritical and len(line):
            criticalLines.append(line)

    return criticalLines


def attackedSquares(colour) -> list:
    pieces = []

    g.attacked = []

    if colour == g.Piece.white:
        pieces = g.whitePieceLocations

    else:
        pieces = g.blackPieceLocations

    for i in pieces:
        if g.board[i] & g.pieceMask == g.Piece.Pawn:
            g.attacked.extend(gm.pawnAttacks((g.board[i], i)))
            continue

        elif g.board[i] & g.pieceMask != g.Piece.King:

            g.attacked.extend(gm.generateMoves((g.board[i], i)))
