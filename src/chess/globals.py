from window import *
import pygame
import os

screen = None


boardImage = pygame.image.load("assets/chessBoard.png")
imageCopy = pygame.image.load("assets/chessBoard.png")


size: float = None
prevSize = 0
weight: float = 0.9
side: float = None
boardSize = 0


board: list = 64 * [0]
squareCentres: list = 64 * [None]

# (<value>, <prevPos>)
heldPiece = ()

takenBlack: list = []
takenWhite: list = []


blackPieceLocations: list = []
whitePieceLocations: list = []


whiteAttackedSquares: list = []
blackAttackedSquares: list = []

# 0 = white
# 1 = black
turn: bool = 0

# 0 = no check
# 1 = check on black
# 2 = check on white
check: int = 0

# k = black king side
# q = black queen side
# K = white king side
# Q = white queen side
canCastle: str = 0


class Piece:

    empty: int = 0
    King: int = 1
    Pawn: int = 2
    Knight: int = 3
    Bishop: int = 4
    Rook: int = 5
    Queen: int = 6

    white: int = 8
    black: int = 16
