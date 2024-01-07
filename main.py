import pygame

from spritesheet import Spritesheet


#Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = SCREEN_WIDTH * 9 / 16



pygame.init()
# pygame.display.set_caption("Pokemon")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sprite = Spritesheet("dinosprites.png", 24, 24)
frames = sprite.parseSpritesheet((0,0,0), 2)
animationCooldown = 100
currentFrame = 0

lastUpdate = pygame.time.get_ticks()

running = True

#Game loop
while running:

    screen.fill((0,0,0))
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate >= animationCooldown:
        currentFrame += 1
        lastUpdate = currentTime
        if currentFrame == 4:
            currentFrame = 0

    screen.blit(frames[currentFrame], (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()