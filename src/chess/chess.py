import pygame
from window import window as w
from chess import globals
from chess import init
from chess import draw
from chess import findSquare as fs
import os

def chess():
    
    # TODO: create the chess game, lol

    pygame.init()
    

    pgWindow = w.PygameWindow(pygame.display.Info().current_w,
                              pygame.display.Info().current_h, "Chess");
    

    running = True;
    
    init.initBoard(pgWindow);
    print(globals.board);
    
    icon = pygame.image.load(os.getcwd() + "/assets/chessButton.png");

    pygame.display.set_icon(icon);
    while(running):
        
        pos = None;

                    

        draw.drawBoard(pgWindow);
        
        currentSqr = fs.findSquare();

        if(currentSqr >= 0):
            pygame.draw.circle(pgWindow.screen, ( 193, 46, 30 ),
                           globals.squareCentres[currentSqr], globals.side / 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            
            if event.type == pygame.MOUSEBUTTONUP and currentSqr >= 0:
                print("(", currentSqr % 8, ", ", int(currentSqr / 8), ")",  sep = '');

        pygame.display.update();
        

    del pgWindow;
