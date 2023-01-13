import pygame, sys, time
import numpy as np


def connectfour():
    clock = pygame.time.Clock()

    pygame.init()

    WIDTH = 700
    HEIGHT = 750
    LINE_WIDTH = 5
    BOARD_ROWS = 7
    BOARD_COLS = 7

    # rgb: red green blue
    RED = (255, 0, 0)
    BG_COLOUR = (0, 0, 0)
    LINE_COLOUR = (255, 255, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect Four")
    screen.fill(BG_COLOUR)

    font = pygame.font.Font("font/Mojangles.ttf", 50)
    piecefont = pygame.font.Font("font/Mojangles.ttf", 90)
    arrow = pygame.image.load("images/arrow.png")

    rectlist = []

    bwin = font.render("Blue Wins!", False, "blue")
    rwin = font.render("Red Wins!", False, "red")
    x = piecefont.render("x", False, "red")
    o = piecefont.render("o", False, "blue")

    bwinr = bwin.get_rect(center=(350, 325))
    rwinr = rwin.get_rect(center=(350, 325))
    rect1 = arrow.get_rect(topleft=(0, 0))
    rect2 = arrow.get_rect(topleft=(100, 0))
    rect3 = arrow.get_rect(topleft=(200, 0))
    rect4 = arrow.get_rect(topleft=(300, 0))
    rect5 = arrow.get_rect(topleft=(400, 0))
    rect6 = arrow.get_rect(topleft=(500, 0))
    rect7 = arrow.get_rect(topleft=(600, 0))

    rectlist.append(rect1)
    rectlist.append(rect2)
    rectlist.append(rect3)
    rectlist.append(rect4)
    rectlist.append(rect5)
    rectlist.append(rect6)
    rectlist.append(rect7)

    # board
    board = np.zeros((BOARD_COLS, BOARD_ROWS))

    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOUR, (0, 50), (700, 50), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 150), (700, 150), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 250), (700, 250), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 350), (700, 350), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 450), (700, 450), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 550), (700, 550), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 650), (700, 650), LINE_WIDTH)

    # vertical lines
    pygame.draw.line(screen, LINE_COLOUR, (100, 50), (100, 650), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (200, 50), (200, 650), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (300, 50), (300, 650), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (400, 50), (400, 650), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (500, 50), (500, 650), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (600, 50), (600, 650), LINE_WIDTH)

    screen.blit(arrow, rect1)
    screen.blit(arrow, rect2)
    screen.blit(arrow, rect3)
    screen.blit(arrow, rect4)
    screen.blit(arrow, rect5)
    screen.blit(arrow, rect6)
    screen.blit(arrow, rect7)

    turn = 0
    kill = 0
    # main loop
    while True:

        # getting mouse position
        mousepos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # turn system
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn % 2 == 0:
                    for col in range(7):
                        if rectlist[col].collidepoint(mousepos):
                            for row in range(5, -1, -1):
                                if board[row][col] == 0:
                                    board[row][col] = 1
                                    break
                            turn += 1
                elif turn % 2 == 1:
                    for col in range(7):
                        if rectlist[col].collidepoint(mousepos):
                            for row in range(5, -1, -1):
                                if board[row][col] == 0:
                                    board[row][col] = 2
                                    break
                            turn += 1

        # pieces are shown on screen
        for row in range(7):
            for col in range(7):
                if board[row][col] == 1:
                    screen.blit(x, ((col * 100) + 20, (row * 100) + 40))
                elif board[row][col] == 2:
                    screen.blit(o, ((col * 100) + 20, (row * 100) + 40))

        for row in range(7):
            for col in range(6):
                # all conditions for winning
                try:
                    if (
                        board[row][col] == 1
                        and board[row + 1][col] == 1
                        and board[row + 2][col] == 1
                        and board[row + 3][col] == 1
                    ):
                        screen.blit(rwin, rwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 1
                        and board[row][col + 1] == 1
                        and board[row][col + 2] == 1
                        and board[row][col + 3] == 1
                    ):
                        screen.blit(rwin, rwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 1
                        and board[row + 1][col + 1] == 1
                        and board[row + 2][col + 2] == 1
                        and board[row + 3][col + 3] == 1
                    ):
                        screen.blit(rwin, rwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 1
                        and board[row + 1][col - 1] == 1
                        and board[row + 2][col - 2] == 1
                        and board[row + 3][col - 3] == 1
                    ):
                        screen.blit(rwin, rwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 2
                        and board[row + 1][col] == 2
                        and board[row + 2][col] == 2
                        and board[row + 3][col] == 2
                    ):
                        screen.blit(bwin, bwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 2
                        and board[row][col + 1] == 2
                        and board[row][col + 2] == 2
                        and board[row][col + 3] == 2
                    ):
                        screen.blit(bwin, bwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 2
                        and board[row + 1][col + 1] == 2
                        and board[row + 2][col + 2] == 2
                        and board[row + 3][col + 3] == 2
                    ):
                        screen.blit(bwin, bwinr)
                        kill += 1
                        break

                    elif (
                        board[row][col] == 2
                        and board[row + 1][col - 1] == 2
                        and board[row + 2][col - 2] == 2
                        and board[row + 3][col - 3] == 2
                    ):
                        screen.blit(bwin, bwinr)
                        kill += 1
                        break

                except:
                    pass

        if kill == 2:
            break

        clock.tick(60)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
