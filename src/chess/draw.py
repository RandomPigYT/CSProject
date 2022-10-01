import pygame
from window import window as w
from chess import globals as g
from chess import util


def drawPieces(window: w.PygameWindow):
    pygame.font.init();
    
    font = pygame.font.SysFont("Adobe Courier", int(g.side / 1.5))
    
    window.screen.blit(font.render("K1", False, (255, 255, 255)),
                       (g.squareCentres[0][0] - (g.side / 2.5),
                        g.squareCentres[0][1] - (g.side / 4)));

    for i in range(len(g.board)):
        pass;
    
isInit = False;

def drawBoard(window: w.PygameWindow):


    window.screen.fill((49, 46, 43))
    
    white: tuple = (240,218,181) 
    black: tuple = (181,135,99)

    
    g.size = pygame.display.get_surface().get_size();
    
    # Math!
    offset: float = (g.size[1] - (g.weight * g.size[1])) / 2;
    size: float= pygame.display.get_surface().get_size();
    boardSize: float = g.size[1] * g.weight;

    g.boardSize = boardSize;
    
    side: int = boardSize / 8;
    g.side = side;
    startPos: tuple = ((g.size[0] - boardSize) / 2, offset);


    calculateCentres = lambda squarePos, side: (squarePos[0] 
                                                + (side / 2), squarePos[1] + (side / 2))


    row: int= 0;
    
    colour = lambda x: white if(x % 2) else black;


     
    # find the centres of the squares
    g.boardImage = pygame.transform.scale(g.imageCopy, (boardSize,
                                                             boardSize));
    while(row < 8):
    
        column: int = 0;
    
        while(column < 8):
            
            g.squareCentres[util.coordsToIndex(7 - row, column)] = calculateCentres((startPos[0] 
                                                                                    + (column * side), 
                                                                                    offset + (row * side)),side)
            column += 1;
        row += 1;
    
    # draw board
    window.screen.blit(g.boardImage, startPos)
    g.prevSize = size;
    drawPieces(window);


    isInit = True;
        
    
