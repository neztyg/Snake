import pygame
import random

pygame.init()

class Snake():
    '''
        Game Title: Retro Snake Game
        Programming Language: Python 3.4
                Modules: pygame

        Credits:
            YOUTUBE --> thenewboston - (Python Game Development)
            
        Programed by:
            Noime Mujires
            Frincess Joy Dolorzo
            Nesty Gem Gordo

        Submitted to: Dr. Riz Rupert Ortiz

        In fulfilment of the 
        Project in 
        Advanced Programming
    '''



    def __init__(me):
        # Screen Dimensions
        me.scr_Width = 800
        me.scr_Height = 600
        me.gameDisplay = pygame.display.set_mode((me.scr_Width,me.scr_Height))

        # Screen Props
        me.clock = pygame.time.Clock()

        me.FPS = 10 # Frames per Second

        #Game Title
        me.gameTitle = "Snake Retro Game"
        pygame.display.set_caption(me.gameTitle)



        # Color Palletes
        me.white = (255,255,255)
        me.black = (0,0,0)
        me.crimson = (255,0,50)
        me.green = (0,110,0)
        me.blue = (50,20,255)

        # Font Sets
        me.xsmallFont = pygame.font.Font("Minercraftory.ttf", 10)
        me.smallFont = pygame.font.Font("Minercraftory.ttf", 25)
        me.medFont = pygame.font.Font("Minercraftory.ttf", 50)
        me.largeFont = pygame.font.Font("Minercraftory.ttf", 80)

        # Image Resources
        me.imgBG = pygame.image.load('bg.png') # Background Image
        me.imgSnake = pygame.image.load('snakeHead.png') # Snake Head Image
        me.imgApple = pygame.image.load('apple2.png') # Apple image

        # Game Constraint dimensions
        me.gameBox = pygame.draw.rect(me.gameDisplay, me.white, [25, 25, me.scr_Width-50, me.scr_Height-50, ])

        pygame.display.flip() #Screen update

        # Dimensions
        # snake block
        me.block_size = 20
        # Apple Thickness
        me.appleThickness = 30
        #Obstacle Thickness
        me.obstacleThick = 50

        # Initial Snake Head direction
        me.Direction = 'right'

        #X n Y Coordinates
        #-Leader/Head of the Snake Object
        me.lead_x = me.scr_Width/2
        me.lead_y = me.scr_Height/2
        #-Change movement of the snake object
        me.lead_x_change = 2
        me.lead_y_change = 0
        #-Apple Random Location
        me.apple_x_Loc = round(random.randrange(25, (me.scr_Width-(25+me.block_size))-me.block_size)/20.0)*20.0
        me.apple_y_Loc = round(random.randrange(25, (me.scr_Height-(25+me.block_size))-me.block_size)/20.0)*20.0

        ####GAMEOVE
        me.gameOver = False

                  
        # Snake Props
        me.snakeList = []
        me.snakeLength = 1

        me.snakeHead =[]
        me.snakeHead.append(me.lead_x)
        me.snakeHead.append(me.lead_y)
        me.snakeList.append(me.snakeHead)

        #LEVEL COUNTER
        me.lvlUP = 1

    def gameLoop(me): # Main Loop of the Game
        # me.startScreen()
        me.Direction = 'right' # Reassign right direction value every gameloop
        snakeList = [] # Reset snake size upon game reload
        snakeLength = 0


        #RESET FRAMES PER SECOND
        me.FPS = 2

        reset = False

        #X n Y Coordinates
        #-Leader/Head of the Snake Object
        me.lead_x = me.scr_Width/2
        me.lead_y = me.scr_Height/2
        #-Change movement of the snake object
        me.lead_x_change = 2
        me.lead_y_change = 0
        #-Apple Random Location
        me.apple_x_Loc = round(random.randrange(25, (me.scr_Width-25)-me.block_size)/20.0)*20.0
        me.apple_y_Loc = round(random.randrange(25, (me.scr_Height-25)-me.block_size)/20.0)*20.0

        gameExit = False
        me.gameOver = False

        # Snake Props
        me.snakeList = []
        me.snakeLength = 1

        me.snakeHead =[]
        me.snakeHead.append(me.lead_x)
        me.snakeHead.append(me.lead_y)
        me.snakeList.append(me.snakeHead)

        # Game Loop
        while not gameExit:
            me.gameOverHandler()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Handle for Quiting the Game
                    me.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        me.pauseGame()
                me.MovekeyEvents(event) # Move key event function call


            # Snake Head Location Change
            me.lead_x += me.lead_x_change
            me.lead_y += me.lead_y_change



            if (me.lead_x+me.block_size > me.scr_Width - me.block_size or 
            me.lead_x < 25 or 
            me.lead_y + me.block_size > me.scr_Height-20 or 
            me.lead_y < 25):
                me.gameOver = True
            
            ##APPLE DRAWN HERE
            me.gameDisplay.blit(me.imgApple, (me.apple_x_Loc, me.apple_y_Loc))


            #######***SNAKE GROW PROPERTY****################
            snakeHead = [] #Clears the 1st block in the snake list
            snakeHead.append(me.lead_x)
            snakeHead.append(me.lead_y)
            if len(snakeList) > snakeLength:
                del snakeList[0]
            snakeList.append(snakeHead)

            me.score(snakeLength)

            # Body collision detection
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    me.gameOver = True

            ##****SNAKE DRAWN HERE****##
            me.snakeObject(me.block_size, snakeList)


            # Apple Eating Functionality
            if (me.lead_x > me.apple_x_Loc and me.lead_x < me.apple_x_Loc + me.appleThickness
                or me.lead_x + me.block_size > me.apple_x_Loc  and  me.lead_x + me.block_size < me.apple_x_Loc + me.appleThickness):
                if me.lead_y > me.apple_y_Loc and me.lead_y < me.apple_y_Loc + me.appleThickness:
                    # print('Eat Apple!!', me.apple_x_Loc , " , " , me.apple_y_Loc)
                    me.apple_x_Loc, me.apple_y_Loc = me.randAppleGen()
                    print(me.apple_x_Loc+ me.appleThickness)
                    snakeLength += 1
                elif me.lead_y + me.block_size > me.apple_y_Loc and me.lead_y + me.block_size < me.apple_y_Loc + me.appleThickness:
                    # print('Eat Apple!!', me.apple_x_Loc , " , " , me.apple_y_Loc)
                    me.apple_x_Loc, me.apple_y_Loc = me.randAppleGen()
                    print(me.apple_x_Loc+me.appleThickness)
                    snakeLength += 1

            pygame.display.update() # Screen update
            me.clock.tick(me.FPS) # Screen update speed

            # Screen Fill with Background
            me.gameDisplay.blit(me.imgBG, (0,0))


            me.levelHandler(snakeLength)

            ####*************OBSTACLE HANDLER****************#####
            me.obstacleBlock(75, 100, 650, 100) # Obstacke 1
            me.obstacleBlock(75, me.scr_Height - 175, 650, 100) # Obstacle 2

            if (me.lead_x + me.block_size > 85 and me.lead_x < me.scr_Width - 85): # Obstacle 1 Handler
                if me.lead_y + me.block_size > 100 and me.lead_y < 200:
                    me.gameOver = True

            if (me.lead_x + me.block_size > 85 and me.lead_x < me.scr_Width - 85): # Obstacle 2 Handler
                if me.lead_y + me.block_size > 420 and me.lead_y < 525:
                    me.gameOver = True

            # Apple to Obstacle Handler
            if (me.apple_x_Loc + me.appleThickness > 75 and me.apple_x_Loc < me.scr_Width - 100):
                if me.apple_y_Loc + me.appleThickness > 100 and me.apple_y_Loc < 200:
                    me.apple_x_Loc, me.apple_y_Loc = me.randAppleGen()     

            if (me.apple_x_Loc + me.appleThickness > 75 and me.apple_x_Loc < me.scr_Width - 80):
                if me.apple_y_Loc + me.appleThickness > 420 and me.apple_y_Loc < 525:
                    me.apple_x_Loc, me.apple_y_Loc = me.randAppleGen()          

        me.quitGame()


####################******START SCREEN EVENT*****########################################
    def startScreen(me):
        intro = True

        while intro:

            me.gameDisplay.fill(me.white)
            me.msg_to_screen("WELCOME to SNAKE",
                          me.green,
                          -100,
                          'medium')
            me.msg_to_screen("The objective of the game is to eat RED APPLES",
                          me.black,
                          -20,
                          'xsmall')
            me.msg_to_screen("Press C to PLAY, P to Pause or Q to QUIT",
                          me.green,
                          20)
            me.msg_to_screen("HAVE FUN!",
                          me.crimson,
                          70,
                          'medium')

            pygame.display.flip()
            me.clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    me.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        me.quitGame()
                    if event.key == pygame.K_c:
                        intro = False
        me.gameLoop()
#########################################################################################

###################*********LEVEL CHANGE HANDLER***********##########################
    def levelHandler(me, snakeLength):
        if me.lvlUP == 1:
            me.FPS = 10
            if snakeLength == 5:
                me.lvlUP += 1
        elif me.lvlUP == 2:
            me.FPS = 15
            if snakeLength == 10:
                me.lvlUP += 1
        elif me.lvlUP == 3:
            me.FPS = 20
            if snakeLength == 10:
                me.lvlUP += 1
        elif me.lvlUP == 4:
            me.FPS = 30

##############################################################################

################*******GAME PAUSE HANDLER********#############################

    def pauseGame(me):
        pause = True

        me.msg_to_screen("GAME PAUSED!!!",
                         me.crimson,
                         -50,
                         "large")
        me.msg_to_screen("Press C to PLAY, P to Pause or Q to QUIT",
                         me.green,
                         20)
        pygame.display.flip()
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    me.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pause = False
                    elif event.key == pygame.K_q:
                        me.quitGame()

#################################################################################

######################************SCORE VIEW**************#################
    def score(me,score):
        # Function for score on the screen
        text = me.xsmallFont.render("Score - " + str(score), True, me.black)
        level = me.xsmallFont.render("Level - " + str(me.lvlUP), True, me.black)
        me.gameDisplay.blit(text, [25,0])
        me.gameDisplay.blit(level, [200,0])
##############################################################################

##################*******OBSTACLE HANDLER*********####################
    def obstacleBlock(me, x_Loc, y_Loc, width, height):
        pygame.draw.rect(me.gameDisplay, me.crimson, [x_Loc, y_Loc, width, height])

####################********GAMEOVER FUNCTION************################################
    def gameOverHandler(me):
        while me.gameOver == True:
            me.gameDisplay.fill(me.white)
            me.msg_to_screen("YOU LOSE!!!",
                          me.crimson,
                          size ='large')
            me.msg_to_screen("Press C to try again or Q too Quit",
                          me.black,
                          60)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    me.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        me.quitGame()
                    if event.key == pygame.K_c:
                        me.lvlUP = 1
                        me.gameLoop()
#####################################################################################

######################****RANDOM APPLE GENERATION********############################
    def randAppleGen(me):
        # Function for generating random location of the apple 
        me.apple_x_Loc = round(random.randrange(25, (me.scr_Width-25)-me.block_size)/20.0)*20.0
        me.apple_y_Loc = round(random.randrange(25, (me.scr_Height-25)-me.block_size)/20.0)*20.0
        return me.apple_x_Loc, me.apple_y_Loc
#####################################################################################

################*****SNAKE OBJECT FUNCTION*********#########################
    def snakeObject(me, block_size, snakeList):
        if me.Direction == "right":
            head = pygame.transform.rotate(me.imgSnake, 270)
        if me.Direction == "left":
            head = pygame.transform.rotate(me.imgSnake, 90)
        if me.Direction == "up":
            head = me.imgSnake
        if me.Direction == "down":
            head = pygame.transform.rotate(me.imgSnake, 180)

        me.gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

        for XnY in snakeList[:-1]:
            pygame.draw.rect(me.gameDisplay, me.green, [XnY[0], XnY[1], block_size, block_size])
############################################################################################

##############*******GAME CONTROL EVENTS HANDLING********##############################
    def MovekeyEvents(me, event):
        # Snake controls ---> Arrow key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                me.Direction = 'left'
                me.lead_x_change = -me.block_size
                me.lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                me.Direction = 'right'
                me.lead_x_change = me.block_size
                me.lead_y_change = 0
            elif event.key == pygame.K_UP:
                me.Direction = 'up'
                me.lead_y_change = -me.block_size
                me.lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                me.Direction = 'down'
                me.lead_y_change = me.block_size
                me.lead_x_change = 0
            elif event.key == pygame.K_p:
                me.pauseGame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                me.lead_y_change = 0
#############################################################################


#################*****GAME OBSTACLE EVENT HANDLING*****######################
    def barrierHandler(me, gameOver):
        if me.lead_x >= me.scr_Width-me.block_size or me.lead_x <= 25 or me.lead_y >= me.scr_Height-me.block_size or me.lead_y <= 25:
            gameOver = True
#############################################################################


##################****GAME OVER EVENT HANDLING****##########################
    def gameOverScreen(me): # Function show text when snake hit an obstacle
        me.gameDisplay.fill(me.white)
        me.msg_to_screen("YOU LOSE!!!",
                      me.crimson,
                      size ='large')
        me.msg_to_screen("Press C to try again or Q too Quit",
                      me.black,
                      60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                me.gameOver = False
                me.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    me.gameExit = True
                    me.gameOver = False
                if event.key == pygame.K_c:
                    me.gameLoop()

#########################################################################3

#################***QUIT FUNCTION****#########################
    def quitGame(me): # Function for quiting Pygame
        pygame.quit()
        quit()
######################################################

###########################SCREEN MESSAGES FUNCTIONS################################
    def text_Object(me, text, color, size): # Function for Text object Properties
        if size == 'xsmall':
            textSuface = me.xsmallFont.render(text, True, color)
        if size == 'small':
            textSuface = me.smallFont.render(text, True, color)
        elif size == 'medium':
            textSuface = me.medFont.render(text, True, color)
        elif size == 'large':
            textSuface = me.largeFont.render(text, True, color)
        return textSuface, textSuface.get_rect()

    def msg_to_screen(me, msg, color, y_displace = 0, size = "small"): # Function for creating text to screen
        textSurf, textRect = me.text_Object(msg, color, size)
        textRect.center = (me.scr_Width/2), (me.scr_Height/2) + y_displace
        me.gameDisplay.blit(textSurf, textRect)
########################################################################################

a = Snake()
a.startScreen()