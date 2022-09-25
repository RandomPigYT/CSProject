import pygame
import tkinter
from window import window as w
from chess import globals
from chess import init


def chess():
    
    # TODO: create the chess game, lol

    pgWindow = w.PygameWindow(1920, 1080, "Chess");
    
    pygame.display.update();

    running = True;
    
    init.initBoard();
    
    while(running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pgWindow.screen.fill((100, 120, 20));
        pygame.display.update();
