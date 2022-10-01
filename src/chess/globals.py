from window import *
import pygame
import os

screen = None;

board: list = 64 * [0];

boardImage = pygame.image.load(os.getcwd() + "/assets/chessBoard.png");
imageCopy = pygame.image.load(os.getcwd() + "/assets/chessBoard.png");

squareCentres: list = 64 * [None]

size: float = None;
prevSize = 0;
weight: float = 0.9;
side: float = None;

takenBlack: list = [];
takenWhite: list  = [];


blackPieceLocations: list = [];
whitePieceLocations: list = [];


attackedSquares: list = [];


turn: bool = 0;

# 0 = no check
# 1 = check on black
# 2 = check on white
check: int = 0; 

# 0 = both can castle
# 1 = only white can castle
# 2 = only black can castle
# 3 = neither can castle
canCastle: bool = 0;

class Piece:

    empty: int = 0;
    King: int = 1;
    Pawn: int = 2;
    Knight: int = 3;
    Bishop: int = 4;
    Rook: int = 5;
    Queen: int = 6;

    white: int = 8;
    black: int = 16;


