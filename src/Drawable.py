
import Screen

import pygame

class Drawable:
    def __init__(self, img, x, y): # x, y: center coordinates
        width  = img.get_width()
        height = img.get_height()
        origin = (x - (width / 2), y - (height / 2))
    
        self.img  = img
        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self, screen):
        Screen.draw_to_screen(screen, self.img, self.rect)