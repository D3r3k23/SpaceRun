
from Drawable import Drawable
from Colors   import *
import Resources

import pygame

POS_X, POS_Y = 80, 700

class Score(Drawable):
    def __init__(self, screen):
        self.font = Resources.load_font('SpaceSquadron', 32)
        self.score = 0

        super().__init__(screen, self.get_img(), POS_X, POS_Y)
    
    def get_img(self):
        return self.font.render('SCORE: ' + str(self.score), True, WHITE)
    
    def update(self, score):
        self.score = score
        self.img = self.get_img()
