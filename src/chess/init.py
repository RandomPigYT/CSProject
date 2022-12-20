from window import window as w
from chess import placePieces as pp
from chess import distToEdge as de
from chess import globals as g
import pygame


def initBoard(window: w.PygameWindow, FEN):

    g.board = 64 * [0]
    g.heldPiece = ()
    g.takenBlack = []
    g.takenWhite = []
    g.blackPieceLocations = []
    g.whitePieceLocations = []
    g.attacked = []
    g.check = 0
    g.check = ""
    g.turn = g.Piece.white
    g.canCastle = 0b1111

    pygame.mixer.init()

    pp.placePieces(FEN)

    de.distToEdge()
