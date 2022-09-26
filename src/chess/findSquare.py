import pygame
from window import window as w
from chess import globals
from chess import init
from chess import draw
import math


def findSquare() -> int:
    
    pos: tuple = pygame.mouse.get_pos();

    distance = lambda p1, p2: math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2));
    
    minDist = 0;
    for i in range(len(globals.squareCentres)):
        
        if(distance(pos, globals.squareCentres[minDist]) > distance(pos,globals.squareCentres[i])):

            minDist = i;
    
    if(distance(pos, globals.squareCentres[minDist]) > globals.side / 2):
        return -1;

    return minDist;


        
