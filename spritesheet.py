import pygame

class Spritesheet:
    def __init__(self, sheet, width, height):
        self.sheet = pygame.image.load(sheet)
        self.width = width
        self.height = height
        self.numberOfFrames = int(self.sheet.get_width() / width)


    def get_frame(self, frameNumber, color, scale):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0,0), (frameNumber * self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width * scale, self.height * scale))
        image.set_colorkey(color)

        return image


    def parseSpritesheet(self, color, scale=1):
        frames = []
        for x in range(self.numberOfFrames):
            frames.append(self.get_frame(x, color, scale))
        return frames