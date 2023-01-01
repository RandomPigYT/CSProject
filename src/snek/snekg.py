# importing libraries
import pygame
import time
import random

def snek():

    snake_speed = 20

    # Window size
    window_x = 720
    window_y = 420


    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    bg = pygame.image.load("images/snake_grass.png")
    rf = pygame.image.load("images/apple.png")
    ##gf = pygame.image.load("images/apple_golden.png")


    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snek')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50]
                ]
    # fruit position
    red_fruit_position = [random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]


    red_fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):

        # creating font object score_font
        score_font = pygame.font.Font(font, size)
        
        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)
        
        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()
        
        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():

        # creating font object my_font
        my_font = pygame.font.Font('font/mojangles.ttf', 50)
        
        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, white)
        
        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (window_x/2, window_y/4)
        
        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the program
        time.sleep(2)
        
        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()


    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_d:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be increased by 1



        
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == red_fruit_position[0] and snake_position[1] == red_fruit_position[1]:
            score += 1
            red_fruit_spawn = False

        else:
            snake_body.pop()
            
        if not red_fruit_spawn:
            red_fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
        
        red_fruit_spawn = True



        
        game_window.blit(bg, (0 , 0))
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        
        

        rfr = rf.get_rect(center = (red_fruit_position[0] , red_fruit_position[1]))
        game_window.blit(rf, rfr)

        # luck = random.randint(1,10)
        # if luck == 1:

        # 	gold_fruit_spawn = True

        # 	noob2 = rf.get_rect(center = (gold_fruit_position[0] , gold_fruit_position[1]))
        # 	game_window.blit(gf, noob2)

        # 	if snake_position[0] == gold_fruit_position[0] and snake_position[1] == gold_fruit_position[1]:
        # 		score += 10
        # 		gold_fruit_spawn = False
                    
        # 	if not gold_fruit_spawn:
        # 		gold_fruit_position = [random.randrange(1, (window_x//10)) * 10,
        # 						random.randrange(1, (window_y//10)) * 10]
        

                

            
        # 	gold_fruit_spawn = True

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score countinuously
        show_score(1, white, 'font/mojangles.ttf', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)
     
