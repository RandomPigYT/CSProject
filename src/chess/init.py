from window import window as w
from chess import globals as g
from chess import placePieces as pp
from chess import distToEdge as de
import pygame


def initBoard(window: w.PygameWindow):

    pygame.mixer.init()

    pp.placePieces("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    de.distToEdge()
