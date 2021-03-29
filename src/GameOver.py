
from Drawable import Drawable
from Colors   import *
import Resources

import pygame

POS_X, POS_Y = 640, 360

class GameOver(Drawable):
    def __init__(self, screen):
        font = Resources.load_font('SpaceSquadron', 44)
        img  = font.render('GAME OVER!', True, RED)
        super().__init__(screen, img, POS_X, POS_Y)
