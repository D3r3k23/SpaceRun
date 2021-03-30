
import Screen
import Resources
import Util

import pygame

SIZE = 150

class Button(Screen.Drawable):
    # Center X and Y coordinates, pygame.Surface
    def __init__(self, name, x, y):
        img_normal = Resources.images[name]
        img_active = Resources.images[name + '_active']

        self.img_normal = pygame.transform.scale(img_normal, (SIZE, SIZE))
        self.img_active = pygame.transform.scale(img_active, (SIZE, SIZE))

        super().__init__(self.img_normal, x, y)
        
        self.hovered = False
    
    def draw(self):
        if self.contains(Util.get_mouse_pos()):
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
