
from Drawable import Drawable
from Util     import *
import Resources

import pygame

class Button(Drawable):
    # Center X and Y coordinates, pygame.Surface
    def __init__(self, screen, x, y, name):
        self.img_normal = Resources.images[name]
        self.img_active = Resources.images[name + '_active']

        width  = self.img_normal.get_width()
        height = self.img_normal.get_height()
        origin = (x - (width / 2), y - (height / 2))
        rect   = pygame.Rect(origin, (width, height))

        super().__init__(screen, self.img_normal, rect)
        self.hovered = False
    
    def draw(self):
        if self.contains(get_mouse_pos()):
            if not self.hovered:
                self.hovered = True
                self.img = self.img_active
        else:
            if self.hovered:
                self.hovered = False
                self.img = self.img_normal

        super().draw()
    
    def contains(self, pos):
        return self.rect.collidepoint(pos)
