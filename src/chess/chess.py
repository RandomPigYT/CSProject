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

    pgWindow = w.PygameWindow(
        pygame.display.Info().current_w, pygame.display.Info().current_h, "Chess"
    )

    running = True

    init.initBoard(pgWindow)

    icon = pygame.image.load(os.getcwd() + "/assets/chessButton.png")

    pygame.display.set_icon(icon)
    while running:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and currentSqr >= 0:
                print("(", currentSqr % 8, ", ", int(currentSqr / 8), ")", sep="")

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    running = False

        draw.drawBoard(pgWindow)
        draw.drawPieces(pgWindow)

        currentSqr = fs.findSquare()

        pygame.display.update()

    del pgWindow
