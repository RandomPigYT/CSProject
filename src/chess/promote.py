from chess import globals as g
from chess import draw
import pygame


def promoteTo(pos, key):

    colour = g.board[pos] & g.colourMask

    if key == pygame.K_q:
        g.board[pos] = g.Piece.Queen | colour
        return True

    if key == pygame.K_n:
        g.board[pos] = g.Piece.Knight | colour
        return True

    if key == pygame.K_r:
        g.board[pos] = g.Piece.Rook | colour
        return True

    if key == pygame.K_b:
        g.board[pos] = g.Piece.Bishop | colour
        return True
    return False


def promotePawn(pos):

    while True:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if promoteTo(pos, event.key):
                    return
