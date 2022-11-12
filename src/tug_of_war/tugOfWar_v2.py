import pygame
from sys import exit
from tug_of_war import globals as g


def init(w, h, title):
    pygame.init()  # starts pygame

    g.screen = pygame.display.set_mode((w, h))  # main window

    pygame.display.set_caption(title)  # title

    g.clock = pygame.time.Clock()  # sets up fps

    g.font = pygame.font.Font("assets/Font/Monocraft.otf", 40)
    g.font2 = pygame.font.Font(
        "assets/Font/Monocraft.otf", 26
    )  # set up fonts for further use

    ico = pygame.image.load("assets/Images/tug_of_war.png").convert_alpha()
    g.floor = pygame.image.load("assets/Images/grass_block_side.png").convert_alpha()
    g.playsurf = pygame.image.load(
        "assets/Images/tug_of_war.png"
    ).convert_alpha()  # loads images

    pygame.display.set_icon(ico)  # uses loaded img as icon

    g.redwin = g.font.render("Red wins!", False, "Red")
    g.bluewin = g.font.render("Blue wins!", False, "Blue")
    g.redkey = g.font2.render("Press z", False, "Red")
    g.bluekey = g.font2.render(
        "Press m", False, "Blue"
    )  # creates text with the font


def pull(force):
    g.playrect.x += force


def draw():
    g.screen.blit(g.sky, (0, 0))
    g.screen.blit(g.border1, (128 + 18, 0))
    g.screen.blit(g.border2, (888 - 22, 0))
    g.screen.blit(g.floor, (0, 384 + 64))
    g.screen.blit(g.playsurf, g.playrect)
    g.screen.blit(g.redkey, (0, 0))
    g.screen.blit(g.bluekey, g.bluerect)  # prints all the assets on the screen


def hasWon():

    if g.playrect.x <= 40:  # check if red has won

        g.screen.blit(
            g.playsurf, g.playrect
        )  # print all assets before showing winner
        g.screen.blit(g.redwin, g.textrectr)  # show 'red wins!' on the screen

        return False

    elif g.playrect.x >= 740:  # check if blue has won

        g.screen.blit(
            g.playsurf, g.playrect
        )  # print all assets before showing winner
        g.screen.blit(g.bluewin, g.textrectb)  # show 'red wins!' on the screen

        return False

    return True


def input(event):

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    if event.type == pygame.KEYDOWN:  # checks if button is pressed

        if event.key == pygame.K_z:  # checks if button was z
            pull(-g.pullForce)

        elif event.key == pygame.K_m:  # checks if button was m
            pull(g.pullForce)


def tugOfWar():

    init(1024, 512, "Tug of war")

    g.sky = pygame.Surface((1024, 512))
    g.sky.fill("Skyblue")  # sky

    g.border1 = pygame.Surface((5, 2000))
    g.border1.fill("Red")  # border for blue

    g.border2 = pygame.Surface((5, 2000))
    g.border2.fill("Blue")  # border for blue

    g.playrect = g.playsurf.get_rect(
        midbottom=(512, 476)
    )  # creates rectangles (hitboxes) for the player image for easy navigation
    g.textrectr = g.redwin.get_rect(midbottom=(512, 200))
    g.textrectb = g.bluewin.get_rect(midbottom=(512, 200))
    g.bluerect = g.bluekey.get_rect(
        topright=(1024, 0)
    )  # creates rectangles (hitboxes) for the font for easy navigation

    loop = True

    while loop:
        for event in pygame.event.get():

            input(event)

        draw()
        loop = hasWon()

        pygame.display.update()
        g.clock.tick(60)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                # allows closing the program after the previous loop is broken
