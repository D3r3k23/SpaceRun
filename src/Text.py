
from Drawable import Drawable
import Resources

import pygame

class Text(Drawable):
    def __init__(self, screen, text, font, size, color, x, y):
        self.font  = Resources.load_font(font, size)
        self.color = color

        img = self.font.render(text, True, color)
        super().__init__(screen, img, x, y)
    
    def change(self, text):
        self.img = self.font.render(text, True, self.color)
