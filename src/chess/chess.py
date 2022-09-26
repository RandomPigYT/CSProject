import pygame
from window import window as w
from chess import globals
from chess import init
from chess import draw
from chess import findSquare as fs
import os

def chess():
    
    # TODO: create the chess game, lol

    pgWindow = w.PygameWindow(1920, 1080, "Chess");
    
    pygame.display.update();

    running = True;
    
    init.initBoard();

    icon = pygame.image.load(os.getcwd() + "/assets/chessButton.png");

    pygame.display.set_icon(icon);
    while(running):
        
        pos = None;

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            

        draw.drawBoard(pgWindow);
        
        currentSqr = fs.findSquare();

        if(currentSqr >= 0):
            pygame.draw.circle(pgWindow.screen, ( 193, 46, 30 ),
                           globals.squareCentres[currentSqr], globals.side / 2)

        pygame.display.update();


    del pgWindow;
