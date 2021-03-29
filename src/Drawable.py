
import pygame

class Drawable:
    def __init__(self, screen, img, x, y):
        self.screen = screen

        width  = img.get_width()
        height = img.get_height()
        origin = (x - (width / 2), y - (height / 2))
    
        self.img  = img
        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self):
        self.screen.blit(self.img, self.rect)
