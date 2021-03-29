
from Text   import Text
from Colors import *
import Resources

import pygame

POS_X, POS_Y = 80, 700

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.text = Text(self.screen, self.get_string(),
            'SpaceSquadron', 32, WHITE, POS_X, POS_Y)
    
    def get_string(self):
        return 'SCORE: ' + str(self.score)
    
    def update(self, score):
        self.score = score
        self.text.change(self.get_string())
    
    def draw(self):
        self.text.draw()
