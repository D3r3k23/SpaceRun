
from Colors import *
import pygame

class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

        # self.font = pygame.font.SysFont(font, fontSize)
        # self.text = self.font.render(text, True, textColor)
    
    def draw(self, screen):
        
