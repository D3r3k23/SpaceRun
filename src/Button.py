
from Colors import *

import pygame

class Button:
    # Center X and Y coordinates, pygame.Surface
    def __init__(self, x, y, image):
        self.image = image
        width = image.get_width()
        height = image.get_height()
        origin = (x - (width / 2), y - (height / 2))

        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def contains(self, pos):
        return self.rect.collidepoint(pos)
