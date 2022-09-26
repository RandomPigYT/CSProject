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

    print(pygame.display.get_surface().get_size())
    
    while(running):
        
        pos = None;

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            
        
        

        draw.drawBoard(pgWindow);

        pygame.display.update();
