import pygame
from window import window as w
from chess import globals as g

def winner(colour, window):

    font = pygame.font.Font("assets/Font/Monocraft.otf", 40)
    
    texts = {g.Piece.white: font.render("White wins", True, (255, 255, 255)),
             g.Piece.black: font.render("Black wins", True, (255, 255, 255))}

    textRect = texts[colour].get_rect()


    while True:
        
        height, width = window.get_size()

        textRect.center = (height // 2, width // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        window.fill((49, 46, 43))

        window.blit(texts[colour], textRect)

        pygame.display.update()


    
