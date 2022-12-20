import pygame

pygame.mixer.init()


screen = None

boardImage = pygame.image.load("assets/chessBoard.png")
imageCopy = pygame.image.load("assets/chessBoard.png")

sSheet = None

moveSound = pygame.mixer.Sound("assets/move.wav")
captureSound = pygame.mixer.Sound("assets/capture.wav")

size: float = None
prevSize = 0
weight: float = 0.9
side: float = None
boardSize = 0


board: list = 64 * [0]

# N, S, E, W, NE, NW, SE, SW
distToEdge: list = []

squareCentres: list = 64 * [0]

# (<value>, <Pos>)
heldPiece = ()

takenBlack: list = []
takenWhite: list = []


blackPieceLocations: list = []
whitePieceLocations: list = []

# 0: while
# 1: black
kingPos = ()

attacked = []

# 0 = no check
# 1 = check on black
# 2 = n white
check: int = 0


# First bit: white king side
# Second bit: white queen side
# Third bit: black king side
# Fourth bit: black queen side
#
# This does not guarantee that castling is possible as the path could be blocked
# by other pieces, or the king could be in check, and etc.
#
# a bit describing the ability to castle to a particular side equals zero if
# the rook on the corresponging side has moved or has been captured.
#
# If the king is moved, all the bits will become zero
canCastle: int = 0b1111


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


colourMask = 0b11000
pieceMask = 0b00111

# 8 = white
# 16 = black
turn: bool = Piece.white
