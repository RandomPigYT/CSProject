from chess import globals as g

# N, S, E, W, NE, NW, SE, SW
directions = [8, -8, 1, -1, 9, 7, -7, -9]


def sliding():
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
                possibleMoves.append(temp);
                break
            
            elif g.board[temp] & 0b11000 == colour:
                possibleMoves.append(temp - directions[i + offset[0]])
                break

    return possibleMoves


def generateMoves() -> list:

    moves = sliding()

    return moves
