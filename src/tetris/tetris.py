from window import window as w
import pygame


def tetris():

    pygame.init()

    pgWindow = w.PygameWindow(
        pygame.display.Info().current_w, pygame.display.Info().current_h, "tetris"
    )

    running = True

    while running:

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
