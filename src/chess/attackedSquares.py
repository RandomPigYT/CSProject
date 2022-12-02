from chess import globals as g
from chess import generateMoves as gm


def getCriticalLine(pos, colour):
    # N, S, E, W, NE, NW, SE, SW
    directions = [8, -8, 1, -1, 9, 7, -7, -9]

    # Movement offset for pieces
    def getPieceOffset(pieceValue):  # {

        piece = pieceValue & 0b00111

        if piece == g.Piece.Rook:
            return (0, 4)
        elif piece == g.Piece.Bishop:
            return (4, 4)
        else:
            return (0, 8)
        
    # }

    def getPiecePossibleDirs(offset, directions) -> list:  # {
        i = offset[0]

        possible = []

        while i < (offset[0] + offset[1]):
            possible.append(directions[i])

            i += 1;

        return possible

    # }
    
    criticalLines = []

    for i in range(len(directions)):
        temp = pos
        numBarriers = 0
        line = []
        isCritical = False


        for j in range(g.distToEdge[pos][i]):


            temp += directions[i]

            if g.board[temp] != 0 and g.board[temp] & 0b11000 == colour:
                numBarriers += 1

            if g.board[temp] != 0 and g.board[temp] & 0b11000 != colour:

                # Check if the piece is attacking the current line
                if (
                    directions[i]
                    in getPiecePossibleDirs(getPieceOffset(g.board[temp]), directions)
                    and numBarriers == 1
                ):
                    isCritical = True

            line.append(temp)
        criticalLines.append(line)
    print(criticalLines)


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
