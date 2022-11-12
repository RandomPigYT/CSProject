import pygame
from sys import exit


class Game:
    screen = None
    clock = None

    font = None
    font2 = None

    floor = None
    playsurf = None

    redwin = None
    bluewin = None
    redkey = None
    bluekey = None

    sky = None
    border1 = None
    border2 = None

    playrect = None
    bluerect = None

    textrectr = None
    textrectb = None

    pullForce = 40


def init(w, h, title):
    pygame.init()  # starts pygame

    Game.screen = pygame.display.set_mode((w, h))  # main window

    pygame.display.set_caption(title)  # title

    Game.clock = pygame.time.Clock()  # sets up fps

    Game.font = pygame.font.Font("assets/Font/Monocraft.otf", 40)
    Game.font2 = pygame.font.Font(
        "assets/Font/Monocraft.otf", 26
    )  # set up fonts for further use

    ico = pygame.image.load("assets/Images/tug_of_war.png").convert_alpha()
    Game.floor = pygame.image.load("assets/Images/grass_block_side.png").convert_alpha()
    Game.playsurf = pygame.image.load(
        "assets/Images/tug_of_war.png"
    ).convert_alpha()  # loads images

    pygame.display.set_icon(ico)  # uses loaded img as icon

    Game.redwin = Game.font.render("Red wins!", False, "Red")
    Game.bluewin = Game.font.render("Blue wins!", False, "Blue")
    Game.redkey = Game.font2.render("Press z", False, "Red")
    Game.bluekey = Game.font2.render("Press m", False, "Blue")  # creates text with the font


def pull(force):
    Game.playrect.x += force


def draw():
    Game.screen.blit(Game.sky, (0, 0))
    Game.screen.blit(Game.border1, (128 + 18, 0))
    Game.screen.blit(Game.border2, (888 - 22, 0))
    Game.screen.blit(Game.floor, (0, 384 + 64))
    Game.screen.blit(Game.playsurf, Game.playrect)
    Game.screen.blit(Game.redkey, (0, 0))
    Game.screen.blit(Game.bluekey, Game.bluerect)  # prints all the assets on the screen


def hasWon():

    if Game.playrect.x <= 40:  # check if red has won

        Game.screen.blit(Game.playsurf, Game.playrect)  # print all assets before showing winner
        Game.screen.blit(Game.redwin, Game.textrectr)  # show 'red wins!' on the screen

        return True

    elif Game.playrect.x >= 740:  # check if blue has won

        Game.screen.blit(Game.playsurf, Game.playrect)  # print all assets before showing winner
        Game.screen.blit(Game.bluewin, Game.textrectb)  # show 'red wins!' on the screen

        return True

    return False


def input(event):

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    if event.type == pygame.KEYDOWN:  # checks if button is pressed

        if event.key == pygame.K_z:  # checks if button was z
            pull(-Game.pullForce)

        elif event.key == pygame.K_m:  # checks if button was m
            pull(Game.pullForce)


def tugOfWar():

    init(1024, 512, "Tug of war")

    Game.sky = pygame.Surface((1024, 512))
    Game.sky.fill("Skyblue")  # sky

    Game.border1 = pygame.Surface((5, 2000))
    Game.border1.fill("Red")  # border for blue

    Game.border2 = pygame.Surface((5, 2000))
    Game.border2.fill("Blue")  # border for blue

    Game.playrect = Game.playsurf.get_rect(
        midbottom=(512, 476)
    )  # creates rectangles (hitboxes) for the player image for easy navigation
    Game.textrectr = Game.redwin.get_rect(midbottom=(512, 200))
    Game.textrectb = Game.bluewin.get_rect(midbottom=(512, 200))
    Game.bluerect = Game.bluekey.get_rect(
        topright=(1024, 0)
    )  # creates rectangles (hitboxes) for the font for easy navigation

    loop = True

    while loop:
        for event in pygame.event.get():

            input(event)

        draw()
        loop = not hasWon()

        pygame.display.update()
        Game.clock.tick(60)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                # allows closing the program after the previous loop is broken
