import pygame
from window import window as w
from chess import init
from chess import draw
from chess import movePiece as mp
from chess import attackedSquares as a
from chess import globals as g
from sprites import sprites as s
from chess import check as ch
from chess import util as u
from chess import findSquare as fs
from chess import winner 
import os


def chess():

    pygame.init()
    pygame.mixer.init()

    pgWindow = w.PygameWindow(
        pygame.display.Info().current_w, pygame.display.Info().current_h, "Chess"
    )

    running = True

    init.initBoard(pgWindow, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    icon = pygame.image.load(os.getcwd() + "/assets/chessButton.png")

    g.sSheet = s.SpriteSheet("assets/piece_sprites.png")

    pygame.display.set_icon(icon)
    while running:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mp.releasePiece()

                if ch.checkmate(g.turn):
                    winner.winner(g.turn ^ g.colourMask, pgWindow.screen)
                    
                    # cleanup
                    pygame.quit()
                    del g.sSheet
                    del pgWindow
                    return
                    

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mp.holdPiece()

        draw.drawBoard(pgWindow)

        # for i in a.getCriticalLines(4, g.Piece.white):
        #    for j in i:
        #        pygame.draw.circle(
        #            pgWindow.screen, (255, 0, 0), g.squareCentres[j], g.side / 3
        #        )

        draw.drawPieces(pgWindow)

        pygame.display.update()

    pygame.quit()
    del g.sSheet
    del pgWindow
    return
