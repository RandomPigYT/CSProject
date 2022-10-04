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

    prevPos = g.heldPiece[1]

    if currentSqr == -1:
        g.board[g.heldPiece[1]] = g.heldPiece[0]
        g.heldPiece = ()
        return

    else:

        temp = g.board[currentSqr]

        g.board[currentSqr] = g.heldPiece[0]
        g.heldPiece = ()

        if currentSqr != prevPos:

            if temp:
                pygame.mixer.Sound.play(g.captureSound)

            else:
                pygame.mixer.Sound.play(g.moveSound)

        return
