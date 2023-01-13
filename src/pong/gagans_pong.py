import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= (
            -1
        )  # if top of the ball is0 or bottom the ball is equal to screen height then reverse vertical ball speed

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= (
            -1
        )  # if left of the ball is 0 or right of the ball is equal to screen width then revrse horizontal ball speed


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


clock = None

# setting up the main window
screen_width = None
screen_height = None
screen = None

# game rectangles(defining rectangles)
ball = None
player = None
opponent = None

bg_color = None
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7


def pong():

    global screen, screen_width, screen_height, clock, screen, ball, player, opponent, bg_color, light_grey, ball_speed_x, ball_speed_y, player_speed, opponent_speed

    # general set-up
    pygame.init()

    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    screen = None

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")

    # game rectangles(defining rectangles)
    ball = pygame.Rect(
        screen_width / 2 - 15, screen_height / 2 - 15, 30, 30
    )  # 15 is subtracted so that ball is at centre
    player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

    bg_color = pygame.Color("grey12")

    while True:
        # handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        ball_animation()
        player_animation()
        opponent_animation()

        # visuals(drawing rectangles)-pygame.draw(surface,color,rect),aaline-antialiasedline
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(
            screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height)
        )

        # updating the window
        pygame.display.flip()
        clock.tick(60)  # limits how fast the loop runs(in this case 60 frames per sec)
