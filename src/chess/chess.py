import pygame
from window import window as w
from chess import init
from chess import draw
from chess import movePiece as mp
from chess import attackedSquares as a
from chess import globals as g
from sprites import sprites as s
import os


def chess():

    pygame.init()
    pygame.mixer.init()

    pgWindow = w.PygameWindow(
        pygame.display.Info().current_w, pygame.display.Info().current_h, "Chess"
    )

    running = True

    init.initBoard(pgWindow)

    icon = pygame.image.load(os.getcwd() + "/assets/chessButton.png")

    g.sSheet = s.SpriteSheet("assets/piece_sprites.png")

    pygame.display.set_icon(icon)
    while running:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                mp.releasePiece()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mp.holdPiece()

        draw.drawBoard(pgWindow)

        for i in a.getCriticalLines(4, g.Piece.white):
            for j in i:
                pygame.draw.circle(
                    pgWindow.screen, (255, 0, 0), g.squareCentres[j], g.side / 3
                )

        draw.drawPieces(pgWindow)

        pygame.display.update()

    pygame.quit()
    del g.sSheet
    del pgWindow
    return
