import pygame
import __colors__
import random
pygame.init()


class Snake():

    def __init__(me):
        me.event = 10

        # Game Title
        gameTitle = 'Retro Snake'

        # Modules Instantiation
        color = __colors__

        clock = pygame.time.Clock()

        # Game Dimension
        disp_width = 800
        disp_height = 600

        # Snake BLOCk dimensions
        snake_size = 20


        FPS = 10 # Speed of the the snake

        direction = "right" #initial direction of image sprite

        # Font Sets
        xsmallFont = pygame.font.Font("Minercraftory.ttf", 10)
        smallFont = pygame.font.Font("Minercraftory.ttf", 25)
        medFont = pygame.font.Font("Minercraftory.ttf", 50)
        largeFont = pygame.font.Font("Minercraftory.ttf", 80)

        # Background Render

        gameDisplay = pygame.display.set_mode((disp_width, disp_height))
        pygame.display.set_caption(gameTitle)


        # pygame.gameDisplay.flip()


        # Image Resources
        icon = pygame.image.load('icon.png') # Icon image
        pygame.display.set_icon(icon)

        imgBG = pygame.image.load('bg.png') # Background Image
        imgSnake = pygame.image.load('snakeHead.png') # Snake Head Image
        imgSnakeTail = pygame.image.load('snakeTail.png') # Snake Tail Image
        imgApple = pygame.image.load('apple.png') # Apple image 
        imgObstacleA = pygame.image.load('obstacleA.png') # Obstacle image with corners
        imgObstaclemid = pygame.image.load('obstacleA.png') # Obstable image in middle


        pygame.display.update()

    def gameQuit():
        pygame.quit()
        quit()

    def pauseGame():
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameQuit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pause = False
                    elif event.key == pygame.K_q:
                        gameQuit()

            #gameDisplay.fill(color.white)
            msg_to_screen("Paused", color.red, -100, 'large')
            msg_to_screen("Press C to Continue or Q to Quit.", color.green, 25)
            pygame.display.update()
            clock.tick(5)


    def randAppleGen():
        # Function for generating random location of the apple 
        apple_x = round(random.randrange(25, (disp_width-25)-snake_size)/20.0)*20.0
        apple_y = round(random.randrange(25, (disp_height-25)-snake_size)/20.0)*20.0
        return apple_x, apple_y

    def score(score):
        # Function for score on the screen
        text = xsmallFont.render("Score  " + str(score), True, color.black)
        gameDisplay.blit(text, [2,0])

    def gameIntro():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameQuit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameQuit()
                    if event.key == pygame.K_c:
                        intro = False
                        # gameLoop()

            gameDisplay.fill(color.white)
            msg_to_screen("WELCOME to SNAKE",
                          color.leaf_green,
                          -100,
                          'medium')
            msg_to_screen("The objective of the game is to eat RED APPLES",
                          color.black,
                          -20,
                          'xsmall')
            msg_to_screen("Press C to PLAY, P to Pause or Q to QUIT",
                          color.green,
                          20)
            msg_to_screen("HAVE FUN!",
                          color.red,
                          70,
                          'medium')

            pygame.display.flip()
            clock.tick(5)



    def snake(snake_size, snakeList):
        if direction == "right":
            head = pygame.transform.rotate(imgSnake, 270)
        if direction == "left":
            head = pygame.transform.rotate(imgSnake, 90)
        if direction == "up":
            head = imgSnake
        if direction == "down":
            head = pygame.transform.rotate(imgSnake, 180)

        gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

        for XnY in snakeList[:-1]:
            pygame.draw.rect(gameDisplay, color.leaf_green, [XnY[0], XnY[1], snake_size, snake_size])

    def text_Object(text, clr, size):
        if size == 'xsmall':
            textSuface = xsmallFont.render(text, True, clr)
        if size == 'small':
            textSuface = smallFont.render(text, True, clr)
        elif size == 'medium':
            textSuface = medFont.render(text, True, clr)
        elif size == 'large':
            textSuface = largeFont.render(text, True, clr)
        return textSuface, textSuface.get_rect()

    def msg_to_screen(me, msg, clr, y_displace = 0, size = "small"):
        textSurf, textRect = text_Object(msg,clr, size)
        textRect.center = (disp_width/2), (disp_height/2) + y_displace
        gameDisplay.blit(textSurf, textRect)

    def obstacle(me,obstacleWidth, obstacleHeight, obstaclelist): #function for obstacle gameover option
        gameDisplay.blit(imgObstaclemid, (obstacle_list[-1][0], obstacle_list[-1][1]))

        for XnY in obstacle_list:
            pygame.draw.rect(gameDisplay, color.black, [XnY[0], XnY(len(obstacle_list)), obstacleWidth, obstacleHeight]) 

        # gameOver = True
        # pygame.draw.rect(gameDisplay, color.black, [obstacleX, obstacleY, obstacleWidth,obstacleHeight]) #obstacle drawing

        # if lead_x >= obstacleX and lead_x <= obstacleX + (obstacleWidth - 10): #Obstacle collision
        #     if lead_y >= obstacleY and lead_y <= obstacleY + (obstacleHeight - 10):
        #         while gameOver == True: #game over text
        #             gameDisplay.fill(color.white)
        #             msg_to_screen("Game Over, C to Play & Q to quit", color.red)
        #             pygame.display.update()

        #             for event in pygame.event.get(): #game over option
        #                 if event.type == pygame.KEYDOWN:
        #                     if event.key == pygame.K_q:
        #                         gameQuit()
        #                     if event.key == pygame.K_c:
        #                         gameLoop()



    def gameLoop(me):
        global direction

        direction = 'right'
        gameExit = False
        gameOver = False

        # Center Object
        lead_x = disp_width / 2
        lead_y = disp_height / 2

        # Lead Change
        lead_x_change = 2
        lead_y_change = 0


        snakeList = []
        snakeLength = 1

        # Apple Object
        appleThickness = 40
        apple_x = round(random.randrange(25, (disp_width-25)-appleThickness)/20.0)*20.0
        apple_y = round(random.randrange(25, (disp_height-25)-appleThickness)/20.0)*20.0

        # Obstacle Variables
        obstacleList = []
        obstacleX = 400 #tryout obstacle
        obstacleY = 100
        obstacleHeight = 100
        obstacleWidth = 20


        # obstacle(obstacleWidth, obstacleHeight, obstacleList)


        while not gameExit:
            while gameOver == True:
                gameDisplay.fill(color.white)
                msg_to_screen("YOU LOSE!!!",
                              color.red,
                              size ='large')
                msg_to_screen("Press C to try again or Q too Quit",
                              color.black,
                              60)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = "right"
                        lead_x_change = snake_size
                        lead_y_change = 0
                    elif event.key == pygame.K_LEFT:
                        direction = "left"
                        lead_x_change = -snake_size
                        lead_y_change = 0

                    elif event.key == pygame.K_UP:
                        direction = "up"
                        lead_y_change = -snake_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        lead_y_change = snake_size
                        lead_x_change = 0
                    elif event.key == pygame.K_p:
                        pauseGame()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        lead_y_change = 0

            if lead_x >= 799 or lead_x <= 0 or lead_y >= 599 or lead_y <= 0:
                gameOver = True

            lead_x += lead_x_change
            lead_y += lead_y_change

            # gameDisplay.fill(color.white)


            # Apple Image Creation
            gameDisplay.blit(imgApple, (apple_x, apple_y))

            # Obstable Image Creation


            snakeHead =[]
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakeList.append(snakeHead)


            if len(snakeList) > snakeLength:
                del snakeList[0]

            # Body collision starter
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True

            snake(snake_size, snakeList) # Draw snake on the screen Function Call
            score(snakeLength - 1)

            pygame.display.update()


            if lead_x > apple_x and lead_x < apple_x + appleThickness or lead_x + snake_size > apple_x  and  lead_x + snake_size < apple_x + appleThickness:
                if lead_y > apple_y and lead_y < apple_y + appleThickness:
                    print('Eat Apple!!')
                    apple_x, apple_y = randAppleGen()
                    snakeLength += 1
                elif lead_y + snake_size > apple_y and lead_y + snake_size < apple_y + appleThickness:
                    print('Eat Apple!!')
                    apple_x, apple_y = randAppleGen()
                    snakeLength += 1

            clock.tick(FPS)
            gameDisplay.blit(imgBG, (0, 0))
        gameQuit()

a = Snake()
a.gameLoop()