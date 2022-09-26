from window import *

screen = None;

board = 64 * [None];

squareCentres: list = 64 * [None]

takenBlack = [];
takenWhite = [];

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

    White: int = 8;
    black: int = 16;


