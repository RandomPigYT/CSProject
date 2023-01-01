def C4():
    import pygame, sys, time
    import numpy as np

    clock=pygame.time.Clock()
    pygame.init()


    WIDTH=700
    HEIGHT=750
    LINE_WIDTH=5
    BOARD_ROWS=6
    BOARD_COLS=7

    #rgb: red green blue
    RED= (255,0,0)
    BG_COLOUR=(0,0,0)
    LINE_COLOUR=(255,255,255)

    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    screen.fill(BG_COLOUR)

    font = pygame.font.Font('src/connect4/font/Mojangles.ttf',50)
    piecefont = pygame.font.Font('src/connect4/font/Mojangles.ttf',90)
    piecefont = pygame.font.Font('src/connect4/font/Mojangles.ttf',90)
    arrow=pygame.image.load('src/connect4/images/arrow.png')

    rectlist=[]

    bwin=font.render('Blue Wins!',False,'blue')
    rwin=font.render('Red Wins!',False,'red')
    rturn=font.render('Red\'s turn',False,'red')
    bturn=font.render('Blue\'s turn',False,'blue')
    x=piecefont.render('x',False,'red')
    o=piecefont.render('o',False,'blue')

    rturnr=rturn.get_rect(midbottom=(350,750))
    bturnr=bturn.get_rect(midbottom=(350,750))
    bwinr=bwin.get_rect(center=(350,325))
    rwinr=rwin.get_rect(center=(350,325))
    rect1=arrow.get_rect(topleft=(0,0))
    rect2=arrow.get_rect(topleft=(100,0))
    rect3=arrow.get_rect(topleft=(200,0))
    rect4=arrow.get_rect(topleft=(300,0))
    rect5=arrow.get_rect(topleft=(400,0))
    rect6=arrow.get_rect(topleft=(500,0))
    rect7=arrow.get_rect(topleft=(600,0))

    rectlist.append(rect1)
    rectlist.append(rect2)
    rectlist.append(rect3)
    rectlist.append(rect4)
    rectlist.append(rect5)
    rectlist.append(rect6)
    rectlist.append(rect7)

    #board
    board=np.zeros((BOARD_ROWS,BOARD_COLS))

    #Horizontal lines
    pygame.draw.line(screen,LINE_COLOUR,(0,50),(700,50),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,150),(700,150),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,250),(700,250),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,350),(700,350),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,450),(700,450),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,550),(700,550),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(0,650),(700,650),LINE_WIDTH)

    #vertical lines
    pygame.draw.line(screen,LINE_COLOUR,(100,50),(100,650),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(200,50),(200,650),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(300,50),(300,650),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(400,50),(400,650),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(500,50),(500,650),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOUR,(600,50),(600,650),LINE_WIDTH)

    screen.blit(arrow,rect1)
    screen.blit(arrow,rect2)
    screen.blit(arrow,rect3)
    screen.blit(arrow,rect4)
    screen.blit(arrow,rect5)
    screen.blit(arrow,rect6)
    screen.blit(arrow,rect7)

    def turnx():
        for c in range(7):
                    if rectlist[c].collidepoint(mousepos):
                        for r in range(5,-1,-1):
                            if board[r][c] == 0:
                                board[r][c] = 1
                                break
    def turno():
        for c in range(7):
                    if rectlist[c].collidepoint(mousepos):
                        for r in range(5,-1,-1):
                            if board[r][c] == 0:
                                board[r][c] = 2
                                break

    turn=0
    kill=0
    #main loop
    while True:

        #getting mouse position
        mousepos=pygame.mouse.get_pos()
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            #turn system
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn%2==0:
                    turnx()
                    turn+=1
                elif turn%2==1:
                    turno()
                    turn+=1

        #pieces are shown on screen
        for row in range(6):
            for col in range(7):
                if board[row][col]==1:
                    screen.blit(x,((col*100)+20,(row*100)+40))
                elif board[row][col]==2:
                    screen.blit(o,((col*100)+20,(row*100)+40))

        clock.tick(60)
        pygame.display.update()

        for winr in range(6):
            for winc in range(7):
                #all conditions for winning
                try:
                    if board[winr][winc] == 1 and board[winr+1][winc] == 1 and board[winr+2][winc] == 1 and board[winr+3][winc] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 1 and board[winr][winc+1] == 1 and board[winr][winc+2] == 1 and board[winr][winc+3] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 1 and board[winr+1][winc+1] == 1 and board[winr+2][winc+2] == 1 and board[winr+3][winc+3] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 1 and board[winr+1][winc-1] == 1 and board[winr+2][winc-2] == 1 and board[winr+3][winc-3] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 1 and board[winr-1][winc+1] == 1 and board[winr-2][winc+2] == 1 and board[winr-3][winc+3] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 1 and board[winr-1][winc-1] == 1 and board[winr-2][winc-2] == 1 and board[winr-3][winc-3] == 1:
                        screen.blit(rwin,rwinr)
                        kill+=1
                        break



                    elif board[winr][winc] == 2 and board[winr+1][winc] == 2 and board[winr+2][winc] == 2 and board[winr+3][winc] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 2 and board[winr][winc+1] == 2 and board[winr][winc+2] == 2 and board[winr][winc+3] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 2 and board[winr+1][winc+1] == 2 and board[winr+2][winc+2] == 2 and board[winr+3][winc+3] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 2 and board[winr+1][winc-1] == 2 and board[winr+2][winc-2] == 2 and board[winr+3][winc-3] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 2 and board[winr-1][winc+1] == 2 and board[winr-2][winc+2] == 2 and board[winr-3][winc+3] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                    elif board[winr][winc] == 2 and board[winr-1][winc-1] == 2 and board[winr-2][winc-2] == 2 and board[winr-3][winc-3] == 2:
                        screen.blit(bwin,bwinr)
                        kill+=1
                        break

                except:
                    pass
                    
        if kill==2:
            time.sleep(2)
            pygame.quit()
            return
