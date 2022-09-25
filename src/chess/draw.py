import pygame
from window import window as w


side: int = 120;
startPos: tuple = (480, 985 - side)


def drawPieces():
    pass


def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((33, 47, 60))
    
    white: tuple = (255, 255, 255) 
    black: tuple = (0, 0, 0)
    
    row: int= 0;
    
    colour = lambda x: black if(x % 2) else white;

    while(row < 8):
        
        column: int = 0;
        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1), (startPos[0] + (column * side), startPos[1] - (row* side), side, side))

            column += 1;

        row += 1;
        
    
