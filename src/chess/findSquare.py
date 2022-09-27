import pygame
from window import window as w
from chess import globals
from chess import init
from chess import draw
import math


def findSquare() -> int:
    
    pos: tuple = pygame.mouse.get_pos();

    for i in range(len(globals.squareCentres)):
        
        bottom = (globals.squareCentres[i][0] - (globals.side / 2), globals.squareCentres[i][1] - (globals.side / 2));

        top = (globals.squareCentres[i][0] + (globals.side / 2),
                  globals.squareCentres[i][1] + (globals.side / 2));

        if((pos[0] > bottom[0] and pos[0] < top[0]) and (pos[1] > bottom[1] and
                                                         pos[1] < top[1])):
            return i;

    return -1;


        
