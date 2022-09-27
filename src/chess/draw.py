import pygame
from window import window as w
from chess import globals
from chess import util
    


def drawPieces():
    pass


def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((33, 47, 60))
    
    white: tuple = (255, 255, 255) 
    black: tuple = (0, 0, 0)

    
    globals.size = pygame.display.get_surface().get_size();
    
    # Math!
    offset: float = (globals.size[1] - (globals.weight * globals.size[1])) / 2;
    size: float= pygame.display.get_surface().get_size();
    boardSize: float = globals.size[1] * globals.weight;
    
    side: int = boardSize / 8;
    globals.side = side;
    startPos: tuple = ((globals.size[0] - boardSize) / 2, globals.size[1] - offset);

    calculateCentres = lambda squarePos, side: (squarePos[0] + (side / 2), squarePos[1] + (side / 2))


    
    row: int= 0;
    
    colour = lambda x: white if(x % 2) else black;

    while(row < 8):

        column: int = 0;

        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1),
                             (startPos[0] + (column * side), ((offset)) + (row * side), side, side))
            
            # find the centres of the squares
            globals.squareCentres[util.coordsToIndex(7 - row, column)] = calculateCentres((startPos[0] + (column * side), offset + (row * side)),side)
            column += 1;

        row += 1;
        
    
