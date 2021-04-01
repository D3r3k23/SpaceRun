
import Screen
import Resources
import Colors
from Text import Text

import pygame

SIZE = 32
POS_X, POS_Y = 12, 680

class Score(Text):
    def __init__(self):
        self.score = 0
        super().__init__(self.get_string(), 'SpaceSquadron', SIZE, Colors.WHITE, POS_X, POS_Y, center=False)
    
    # Makes current score into string
    def get_string(self):
        return 'SCORE: ' + str(self.score)
    
    # Sets the score and updates Text object
    def set_score(self, score):
        self.score = score
        self.text = self.get_string()
        super().update()
