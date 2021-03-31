
from GameObject import GameObject
import Resources
import Util
import Config

from math import sqrt
from time import time
import pygame

START_X, START_Y = 200, 120

ACCEL_FACTOR = 36
SPEED_FACTOR = 20

MAX_SPEED = 25

crashSound = Resources.sounds['Explosion']

class Player(GameObject):
    def __init__(self):
        img = Resources.images['Spaceship']
        super().__init__(img, START_X, START_Y)

        self.posY  = START_Y
        self.velY  = 0.0
        self.acelY = 0.0

        self.score = 0
        self.alive = True
    
    def move(self, ts):
        if self.alive:
            if Util.is_key_pressed(pygame.K_SPACE):
                self.acelY = -1.0
            else:
                self.acelY = 1.0

        self.velY += ACCEL_FACTOR * self.acelY * ts
        self.velY = Util.clamp(self.velY, -MAX_SPEED, MAX_SPEED)

        self.posY += SPEED_FACTOR * self.velY * ts

        self.rect.centery = self.posY
    
    def kill(self, explode=False):
        self.alive = False
        self.acelY = 0.0
        self.velY  = 0.0

        if explode:
            self.img = Resources.images['Explosion5']
            crashSound.play()
    
    def is_alive(self):
        return self.alive
    
    def in_bounds(self):
        return (-20 < self.rect.bottom) and (self.rect.top < Config.SCREEN_HEIGHT)

    def get_score(self):
        return self.score
    
    def inc_score(self):
        self.score += 1
    
    def get_speed(self):
        return sqrt(self.score)
