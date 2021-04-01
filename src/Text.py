
import Screen
import Resources

import pygame

# Drawable text object
class Text(Screen.Drawable):
    def __init__(self, text, font, size, color, x, y, center=False):
        self.font  = Resources.load_font(font, size)
        self.color = color
        self.text  = text

        img = Text.make_img(self.font, text, color)
        super().__init__(img, x, y, center)
    
    # Updates the image
    def update(self):
        self.img = Text.make_img(self.font, self.text, self.color)

    # Make image from text and color using font
    @staticmethod
    def make_img(font, text, color):
        return font.render(text, True, color)
