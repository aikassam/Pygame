#Personal project utilizing Pygame to create a platformer game. I use royalty-free tilesets and sprites found online. This project serves as a way to practice OOP principles, while also creating something fun.

#Spritesheet created by @ScissorMarks on Twitter.

import pygame
from spritesheet import Spritesheet


#Defining global constants for screen width and height to be used later.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = SCREEN_WIDTH * 9 / 16


#Initializing Pygame game.
pygame.init()
# pygame.display.set_caption("Pokemon")


#Defining size of the screen.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#Importing and parsing spritesheet into array. Using tick functions to iterate through frames.
sprite = Spritesheet("dinosprites.png", 24, 24)
frames = sprite.parseSpritesheet((0,0,0), 2)
animationCooldown = 100
currentFrame = 0
lastUpdate = pygame.time.get_ticks()

#Parsing array of all frames into different actions (running, jumping, hurt, etc.). Each index in the animation list will contain a subarray of all frames for one specific action. Each action will be assigned to a number arbitrarily and will be controlled by the variable "action" (action = 0 means the player is currently idle).
animationList = []
framesPerActionList = [4, 6, 3, 4]
action = 0;
stepCounter = 0

#Assigns a list of frames to each index in animationList.
for framesPerAction in framesPerActionList:
    tempImgList = []
    for _ in range(framesPerAction):
        tempImgList.append(frames[stepCounter])
        stepCounter += 1
    animationList.append(tempImgList)
   
    
running = True

#Game loop
while running:

    screen.fill((0,0,0))
    currentTime = pygame.time.get_ticks()

    #Updating frames for idle animation at frequency of perviously defined animation cooldown.
    if currentTime - lastUpdate >= animationCooldown:
        currentFrame += 1
        lastUpdate = currentTime
    if currentFrame == len(animationList[0]):
        currentFrame = 0
    screen.blit(animationList[2][currentFrame], (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()