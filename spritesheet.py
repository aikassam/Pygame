#Class object dedicated to loading and parsing spritesheet for character animation, and storing individual frames in an array.

#The array parsed will contain all frames within the spritesheet, which can then be separated later into subarrays of frames for idle, movement, jumping, etc.

#For now, this class is designed assuming the spritesheet will only list out frames horizontally, and that all frames are equal size.

import pygame




#Imports spritesheet image file. Width and height will be the dimensions of each individual frame (if each frame is 24x24 pixels, input width = 24, height = 24)
class Spritesheet:
    def __init__(self, sheet, width, height):
        self.sheet = pygame.image.load(sheet)
        self.width = width
        self.height = height
        self.numberOfFrames = int(self.sheet.get_width() / width)

#Internally used method, extracts single frame from a spritesheet and returns it as a Pygame surface. Assuming frames are ordered from left to right, starting at 0, returns frame based on frameNumber input.
    def get_frame(self, frameNumber, color, scale):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0,0), (frameNumber * self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width * scale, self.height * scale))
        image.set_colorkey(color)

        return image

#Iterates through spritesheet, uses get_frame method to store all frames inside an array and returns the array.
    def parseSpritesheet(self, color, scale=1):
        frames = []
        for frame in range(self.numberOfFrames):
            frames.append(self.get_frame(frame, color, scale))
        return frames