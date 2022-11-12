from chess import globals as g
from chess import util as u

# N, S, E, W, NE, NW, SE, SW
directions = [8, -8, 1, -1, 9, 7, -7, -9]


def distCmp(currentDist, condition):
    for i in range(len(condition)):
        if not currentDist[i] >= condition[i]:
            return False

    return True


def knight() -> list:

    pos = g.heldPiece[1]
    colour = g.heldPiece[0] & 0b11000

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

    # Generate a list of positions satisfying the condition
    possibleLocations = [
        x for i, x in enumerate(moveLocations) if distCmp(currentDist, conditions[i])
    ]

    # The actual moves, possibleLocations is just the offset from current position
    possibleMoves = []

    for i in possibleLocations:
        possibleMoves.append(pos + i)

    return possibleMoves


def pawns() -> list:

    pos = g.heldPiece[1]
    colour = g.heldPiece[0] & 0b11000

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
        if (
            g.board[pos + (colourMod(colour) * directions[4])] & 0b11000 != colour
            and g.board[pos + (colourMod(colour) * directions[4])] != 0
        ):
            possibleMoves.append(pos + (colourMod(colour) * directions[4]))

        if (
            g.board[pos + (colourMod(colour) * directions[5])] & 0b11000 != colour
            and g.board[pos + (colourMod(colour) * directions[5])] != 0
        ):
            possibleMoves.append(pos + (colourMod(colour) * directions[5]))

    return possibleMoves


def sliding() -> list:

    piece = g.heldPiece[0] & 0b00111
    pos = g.heldPiece[1]
    colour = g.heldPiece[0] & 0b11000

    offset = ()

    possibleMoves = []

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

            if g.board[temp] == 0:
                possibleMoves.append(temp)

            elif g.board[temp] & 0b11000 != colour:
                possibleMoves.append(temp)
                break

            elif g.board[temp] & 0b11000 == colour:
                possibleMoves.append(temp - directions[i + offset[0]])
                break

    return possibleMoves


def generateMoves() -> list:

    moves = list(range(len(g.board)))

    if g.heldPiece[0] & 0b00111 >= g.Piece.Bishop:
        moves = sliding()

    elif g.heldPiece[0] & 0b00111 == g.Piece.Pawn:
        moves = pawns()

    elif g.heldPiece[0] & 0b00111 == g.Piece.Knight:
        moves = knight()

    return moves
