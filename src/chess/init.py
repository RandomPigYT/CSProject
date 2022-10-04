from window import window as w
from chess import globals as g
from chess import placePieces as pp
import pygame


def initBoard(window: w.PygameWindow):
    
    pygame.mixer.init()

    pygame.mixer.music.set_volume(0.7)
    pp.placePieces("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
