from chess import globals as g
from chess import findSquare as fs
from chess import makeMove as mm
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

    # This is to prevent sound from playing if end position is the same as
    # start position
    temp = g.board[currentSqr]

    if mm.makeMove(g.heldPiece[1], currentSqr):

        if currentSqr != prevPos:

            # Switch turns
            g.turn ^= g.colourMask

            # Don't play sound if starting square is the same as the ending
            # square
            if temp:
                pygame.mixer.Sound.play(g.captureSound)
            else:
                pygame.mixer.Sound.play(g.moveSound)

    return
