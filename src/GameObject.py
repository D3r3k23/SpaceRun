
from Drawable import Drawable
from Colors   import *

import pygame

class GameObject(Drawable):
    SHOW_HITBOXES = True

    @classmethod
    def toggle_hitboxes(cls):
        cls.SHOW_HITBOXES = not cls.SHOW_HITBOXES
        print(cls.SHOW_HITBOXES)

    def __init__(self, screen, img, x, y):
        super().__init__(screen, img, x, y)

        self.hitbox = self.rect
    
    def draw(self):
        super().draw()
        if self.SHOW_HITBOXES:
            pygame.draw.rect(self.screen, GRAY, self.hitbox, width=1)

    def get_hitbox(self):
        return self.hitbox
