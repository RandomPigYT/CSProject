import pygame
from window import window as w
from chess import globals as g
from chess import util


def drawPieces(window: w.PygameWindow):
    pygame.font.init();
    
    font = pygame.font.SysFont("Adobe Courier", int(g.side))
    
    window.screen.blit(font.render("Hello", False, (255, 255, 255)), (0, 0));

    for i in range(len(g.board)):
        pass;
    
    



def drawBoard(window: w.PygameWindow):
    
    window.screen.fill((49, 46, 43))
    
    white: tuple = (240,218,181) 
    black: tuple = (181,135,99)

    
    g.size = pygame.display.get_surface().get_size();
    
    # Math!
    offset: float = (g.size[1] - (g.weight * g.size[1])) / 2;
    size: float= pygame.display.get_surface().get_size();
    boardSize: float = g.size[1] * g.weight;
    
    side: int = boardSize / 8;
    g.side = side;
    startPos: tuple = ((g.size[0] - boardSize) / 2, g.size[1] - offset);

    calculateCentres = lambda squarePos, side: (squarePos[0] + (side / 2), squarePos[1] + (side / 2))


    
    row: int= 0;
    
    colour = lambda x: white if(x % 2) else black;

    while(row < 8):

        column: int = 0;

        while(column < 8):
            pygame.draw.rect(window.screen, colour(column + row + 1),
                             (startPos[0] + (column * side), ((offset)) + (row * side), side, side))
            
            # find the centres of the squares
            if(g.prevSize != size):
                g.squareCentres[util.coordsToIndex(7 - row, column)] = calculateCentres((startPos[0] + (column * side), offset + (row * side)),side)
                print("changed size", size)
            column += 1;

        row += 1;

    g.prevSize = size;
    drawPieces(window);
        
    
