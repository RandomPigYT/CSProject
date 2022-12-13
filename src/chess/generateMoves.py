from chess import globals as g
from chess import util as u

# N, S, E, W, NE, NW, SE, SW
directions = [8, -8, 1, -1, 9, 7, -7, -9]


def king(pieceData: tuple) -> list:
    pos = pieceData[1]

    moves = []

    for i in range(len(directions)):
        if g.distToEdge[pos][i] >= 1:
            if pos + directions[i] not in g.attacked:
                moves.append(pos + directions[i])
    return moves


def knight(pieceData: tuple) -> list:

    pos = pieceData[1]

    # Possible offsets (NNE EEN SSE EES NNW WWN SSW WWS)
    moveLocations = [17, 10, -15, -6, 15, 6, -17, -10]
    conditions = [
        (2, 0, 1, 0),
        (1, 0, 2, 0),
        (0, 2, 1, 0),
        (0, 1, 2, 0),
        (2, 0, 0, 1),
        (1, 0, 0, 2),
        (0, 2, 0, 1),
        (0, 1, 0, 2),
    ]  # Distance reqired to be able to move (N, S, E, W)

    currentDist = g.distToEdge[pos][0:4]

    def distCmp(currentDist, condition):  # {
        for i in range(len(condition)):
            if not currentDist[i] >= condition[i]:
                return False

        return True

    # }

    # Generate a list of positions satisfying the condition
    # List comprehension is tight.
    possibleLocations = [
        x for i, x in enumerate(moveLocations) if distCmp(currentDist, conditions[i])
    ]

    # The actual moves, possibleLocations is just the offset from current position
    possibleMoves = []

    for i in possibleLocations:
        possibleMoves.append(pos + i)

    return possibleMoves


def pawnAttacks(pieceData: tuple) -> list:

    pos = pieceData[1]
    colour = pieceData[0] & g.colourMask

    possibleMoves = []

    # This is so that the offset is negative for black pieces
    colourMod = lambda colour: 1 if (colour == g.Piece.white) else -1

    inFinalRank = (
        lambda colour, pos: True
        if (colour == g.Piece.white and u.indexToCoords(pos)[1] == 7)
        or (colour == g.Piece.black and u.indexToCoords(pos)[1] == 0)
        else False
    )

    # Attacked squares
    if not inFinalRank(colour, pos):
        if g.distToEdge[pos][2] != 0:
            if colour == g.Piece.white:
                possibleMoves.append(pos + (colourMod(colour) * directions[4]))
            else:
                possibleMoves.append(pos + (colourMod(colour) * directions[5]))

        if g.distToEdge[pos][3] != 0:
            if colour == g.Piece.white:
                possibleMoves.append(pos + (colourMod(colour) * directions[5]))
            else:
                possibleMoves.append(pos + (colourMod(colour) * directions[4]))

    return possibleMoves


def pawns(pieceData: tuple) -> list:

    pos = pieceData[1]
    colour = pieceData[0] & g.colourMask

    possibleMoves = []

    inInitialRank = (
        lambda colour, pos: True
        if (colour == g.Piece.white and u.indexToCoords(pos)[1] == 1)
        or (colour == g.Piece.black and u.indexToCoords(pos)[1] == 6)
        else False
    )

    inFinalRank = (
        lambda colour, pos: True
        if (colour == g.Piece.white and u.indexToCoords(pos)[1] == 7)
        or (colour == g.Piece.black and u.indexToCoords(pos)[1] == 0)
        else False
    )

    # This is so that the offset is negative for black pieces
    colourMod = lambda colour: 1 if (colour == g.Piece.white) else -1

    # check for double pawn push
    if (
        inInitialRank(colour, pos)
        and g.board[pos + (colourMod(colour) * (2 * directions[0]))] == 0
        and g.board[pos + (colourMod(colour) * (1 * directions[0]))] == 0
    ):
        possibleMoves.append(pos + (colourMod(colour) * (2 * directions[0])))

    # check for single pawn push
    if (
        not inFinalRank(colour, pos)
        and g.board[pos + (colourMod(colour) * directions[0])] == 0
    ):
        possibleMoves.append(pos + (colourMod(colour) * directions[0]))

    # TODO: check for en passant

    # check captures
    if not inFinalRank(colour, pos):
        if g.board[pos + (colourMod(colour) * directions[4])] != 0:
            possibleMoves.append(pos + (colourMod(colour) * directions[4]))

        if g.board[pos + (colourMod(colour) * directions[5])] != 0:
            possibleMoves.append(pos + (colourMod(colour) * directions[5]))

    return possibleMoves


def sliding(pieceData: tuple) -> list:

    piece = pieceData[0] & g.pieceMask
    pos = pieceData[1]
    colour = pieceData[0] & g.colourMask

    offset = ()

    possibleMoves = []

    # This decides which directions the piece can move in
    # offset[0] is the first direction
    # offset[1] is the number of directions
    if piece == g.Piece.Rook:
        offset = (0, 4)
    elif piece == g.Piece.Bishop:
        offset = (4, 4)
    else:
        offset = (0, 8)

    for i in range(offset[1]):

        temp = pos

        for j in range(g.distToEdge[pos][i + offset[0]]):
            temp += directions[i + offset[0]]

            # Check if the current square is empty
            if g.board[temp] == 0:
                possibleMoves.append(temp)

            # Check if the current sqaure contains a piece of the same colour
            else:
                possibleMoves.append(temp)
                break

        # elif g.board[temp] & g.colourMask == colour:
        #    possibleMoves.append(temp - directions[i + offset[0]])
        #    break

    return possibleMoves


def generateMoves(pieceData: tuple) -> list:

    moves = list(range(len(g.board)))

    if pieceData[0] & g.pieceMask >= g.Piece.Bishop:
        moves = sliding(pieceData)

    elif pieceData[0] & g.pieceMask == g.Piece.Pawn:
        moves = pawns(pieceData)

    elif pieceData[0] & g.pieceMask == g.Piece.Knight:
        moves = knight(pieceData)

    elif pieceData[0] & g.pieceMask == g.Piece.King:
        moves = king(pieceData)

    return moves
