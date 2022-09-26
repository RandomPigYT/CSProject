import pygame
from window import window as w
from chess import globals

    


def drawPieces():
    pass


def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((33, 47, 60))
    
    white: tuple = (255, 255, 255) 
    black: tuple = (0, 0, 0)

    weight: float = 0.9
    
    size:float = pygame.display.get_surface().get_size();
    
    # Math!
    offset: float = (size[1] - (weight * size[1])) / 2;
    size: float= pygame.display.get_surface().get_size();
    boardSize: float= size[1] * weight;
    
    side: int = boardSize / 8;
    startPos: tuple = ((size[0] - boardSize) / 2, size[1] - offset);

    calculateCentres = lambda squarePos, side: (squarePos[0] + (side / 2), squarePos[1] + (side / 2))

    coordsToIndex = lambda row, column: row * 8 + column

    
    row: int= 0;
    
    colour = lambda x: white if(x % 2) else black;

    while(row < 8):

        column: int = 0;

        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1),
                             (startPos[0] + (column * side), ((offset)) + (row * side), side, side))
            
            # find the centres of the squares
            globals.squareCentres[coordsToIndex(row, column)] = calculateCentres((startPos[0] + (column * side), offset + (row * side)),side)
            column += 1;

        row += 1;
        
    
