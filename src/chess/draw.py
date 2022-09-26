import pygame
from window import window as w




def drawPieces():
    pass


def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((33, 47, 60))
    
    white: tuple = (255, 255, 255) 
    black: tuple = (0, 0, 0)

    weight = 0.9
    
    size = pygame.display.get_surface().get_size();
    offset = (size[1] - (weight * size[1])) / 2;
    size = pygame.display.get_surface().get_size();
    boardSize = size[1] * weight;
    
    side: int = boardSize / 8;
    startPos: tuple = ((size[0] - boardSize) / 2, size[1] - offset);

    #pygame.draw.rect(window.screen, white, (startPos[0], offset, boardSize, boardSize))
    
    row: int= 0;
    
    colour = lambda x: white if(x % 2) else black;

    while(row < 8):
        
        column: int = 0;
        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1),
                             (startPos[0] + (column * side), ((offset)) + (row * side), side, side))

            column += 1;

        row += 1;
        
    
