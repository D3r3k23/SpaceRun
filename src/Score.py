
from Text import Text
import Colors
import Resources

import pygame

POS_X, POS_Y = 80, 700

class Score(Text):
    def __init__(self):
        self.score = 0
        super().__init__(self.get_string(), 'SpaceSquadron', 32, Colors.WHITE, POS_X, POS_Y)
    
    def get_string(self):
        return 'SCORE: ' + str(self.score)
    
    def set_score(self, score):
        self.score = score
        self.text = self.get_string()
        super().update()
