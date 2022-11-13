from chess import globals as g
from chess import findSquare as fs
from chess import findLegalMoves as flm
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

    # Check if move is illegal or it is not the right player's turn
    if (
        currentSqr == -1
        or not flm.isLegalMove(g.heldPiece[1], currentSqr)
        or (g.heldPiece[0] & 0b11000) != g.turn
    ):

        g.board[g.heldPiece[1]] = g.heldPiece[0]
        g.heldPiece = ()
        return

    else:
        # This is to prevent sound from playing if end position is the same as
        # start position
        temp = g.board[currentSqr]

        g.board[currentSqr] = g.heldPiece[0]
        g.heldPiece = ()


        if currentSqr != prevPos:

            # Switch turns
            g.turn ^= 0b11000

            if temp:
                pygame.mixer.Sound.play(g.captureSound)
            else:
                pygame.mixer.Sound.play(g.moveSound)

    return
