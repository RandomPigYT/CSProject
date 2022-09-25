from window import *

screen = None;

board = 64 * [None];

takenBlack = [];
takenWhite = [];

turn: bool = 0;

# 0 = no check
# 1 = check on black
# 2 = check on white
check: int = 0;                 

