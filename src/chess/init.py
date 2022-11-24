from window import window as w
from chess import placePieces as pp
from chess import distToEdge as de
from chess import globals as g
import pygame


def initBoard(window: w.PygameWindow):

    g.board = 64 * [0]

    pygame.mixer.init()

    pp.placePieces("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    de.distToEdge()
