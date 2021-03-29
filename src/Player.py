
from Drawable import Drawable
import Resources
from Util import *

from math import sqrt
from time import time
import pygame

START_X, START_Y = 200, 120

ACCEL_FACTOR = 36
SPEED_FACTOR = 20

MAX_SPEED = 25

class Player(Drawable):
    def __init__(self, screen):
        img = Resources.images['Spaceship']

        super().__init__(screen, img, START_X, START_Y)

        self.posY  = START_Y
        self.velY  = 0.0
        self.acelY = 0.0

        self.score = 0
        self.alive = True
    
    def move(self, ts):
        if is_key_pressed(pygame.K_SPACE):
            self.acelY = -1.0
        else:
            self.acelY = 1.0

        self.velY += ACCEL_FACTOR * self.acelY * ts
        self.velY = clamp(self.velY, -MAX_SPEED, MAX_SPEED)

        self.posY += SPEED_FACTOR * self.velY * ts

        self.rect.centery = self.posY
    
    def kill(self):
        self.alive = False
        self.timeOfDeath = time()
    
    def is_alive(self):
        return self.alive
    
    def in_bounds(self):
        return (-20 < self.rect.bottom) and (self.rect.top < self.screen.get_height())

    def get_score(self):
        return self.score
    
    def inc_score(self):
        self.score += 1
        print(self.score)
    
    def get_speed(self):
        return sqrt(self.score)
