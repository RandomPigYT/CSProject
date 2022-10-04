from chess import globals as g
from chess import findSquare as fs
import pygame


def holdPiece():

    currentSqr = fs.findSquare()

    if currentSqr == -1 or g.board[currentSqr] == 0:
        return

    g.heldPiece = (g.board[currentSqr], currentSqr)

    g.board[currentSqr] = 0


def releasePiece():

    currentSqr = fs.findSquare()

    if len(g.heldPiece) == 0:
        return

    if currentSqr == -1:
        g.board[g.heldPiece[1]] = g.heldPiece[0]
        g.heldPiece = ()
        return

    else:
        g.board[currentSqr] = g.heldPiece[0]
        g.heldPiece = ()
        return