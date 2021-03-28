
from Drawable import Drawable

import pygame

class Button(Drawable):
    # Center X and Y coordinates, pygame.Surface
    def __init__(self, screen, x, y, img):
        width  = img.get_width()
        height = img.get_height()
        origin = (x - (width / 2), y - (height / 2))
        rect   = pygame.Rect(origin, (width, height))

        super().__init__(screen, img, rect)
    
    def contains(self, pos):
        return self.rect.collidepoint(pos)
