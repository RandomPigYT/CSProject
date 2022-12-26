from chess import util as u
from chess import globals as g
from chess import generateMoves as gm
from chess import attackedSquares as a


def isCheck() -> bool:

    a.attackedSquares(g.turn ^ g.colourMask)

    kingPos = u.findKing(g.turn)

    if kingPos in g.attacked:
        return True


def makeTempMove(startSquare, endSquare):
    boardCopy = g.board.copy()

    if len(g.heldPiece) and g.heldPiece[1] == startSquare:
        piece = g.heldPiece[0]

    else:
        piece = g.board[startSquare]

    if not piece & g.colourMask == g.board[endSquare] & g.colourMask:
        g.board[startSquare] = 0
        g.board[endSquare] = piece

    return boardCopy


def unmakeMove(boardCopy: list):
    g.board = boardCopy.copy()


def checkmate(colour):
    for i in range(len(g.board)):

        if g.board[i] and g.board[i] & g.colourMask == colour:
            moves = gm.generateMoves((g.board[i], i))

            legalMoves = []

            for j in moves:
                boardCopy = makeTempMove(i, j)

                if not isCheck():
                    legalMoves.append(j)

                unmakeMove(boardCopy)

            if len(legalMoves):
                return False
    return True
