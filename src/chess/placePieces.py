from chess import globals
from chess import util


values = {"k": 1, "p": 2, "n": 3, "b": 4, "r": 5, "q": 6}


def placePieces(FEN: str):

    row: int = 7
    column: int = 0

    for i in FEN:

        if i.isdigit():
            column += int(i)

        if i.isalpha():

            if i.isupper():
                globals.board[util.coordsToIndex(row, column)] = (
                    globals.Piece.white | values[i.lower()]
                )

            else:
                globals.board[util.coordsToIndex(row, column)] = (
                    globals.Piece.black | values[i]
                )

            column += 1

        if i == "/":
            row -= 1
            column = 0
