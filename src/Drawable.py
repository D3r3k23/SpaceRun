
import pygame

class Drawable:
    def __init__(self, screen, img, rect):
        self.screen = screen
        self.img    = img
        self.rect   = rect
    
    def draw(self):
        self.screen.blit(self.img, self.rect)
