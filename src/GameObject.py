
from Drawable import Drawable
import Colors

import pygame

class GameObject(Drawable):
    SHOW_HITBOXES = True

    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.hitbox = self.rect
    
    def draw(self, screen):
        super().draw(screen)
        if GameObject.SHOW_HITBOXES:
            pygame.draw.rect(screen, Colors.GRAY, self.hitbox, width=1) # Screen???

    def get_hitbox(self):
        return self.hitbox

    @classmethod
    def toggle_hitboxes(cls):
        cls.SHOW_HITBOXES = not cls.SHOW_HITBOXES
