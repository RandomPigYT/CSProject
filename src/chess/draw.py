import pygame
from window import window as w

def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((33, 47, 60))
    
    white = (255, 255, 255) 
    black = (0, 0, 0)
    side = 120;
    
    row = 0;
    
    colour = lambda x: black if(x % 2) else white;

    startPos = (480, 985 - side)
    while(row < 8):
        
        column = 0;
        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1), (startPos[0] + (column * side), startPos[1] - (row* side), side, side))

            column += 1;

        row += 1;
        
    
