
from Drawable import Drawable
import Resources

import pygame

class Text(Drawable):
    def __init__(self, text, font, size, color, x, y):
        self.font  = Resources.load_font(font, size)
        self.color = color
        self.text  = text

        img = Text.make_img(self.font, text, color)
        super().__init__(img, x, y)
    
    def set_text(self, text):
        self.text = text
    
    def update(self):
        self.img = Text.make_img(self.font, self.text, self.color)

    @staticmethod
    def make_img(font, text, color):
        return font.render(text, True, color)
