import pygame
import tkinter
from window import window as w
from chess import globals
from chess import init
from chess import draw
import os

def chess():
    
    # TODO: create the chess game, lol

    pgWindow = w.PygameWindow(1920, 1080, "Chess");
    
    pygame.display.update();

    running = True;
    
    init.initBoard();

    
    while(running):
        
        pos = None;

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            

        draw.drawBoard(pgWindow);

        for i in globals.squareCentres:
            pygame.draw.circle(pgWindow.screen, ( 193, 46, 30 ), (i[0], i[1]), 50)

        pygame.display.update();
