
import Screen
import Resources
import Util
from GameObject import GameObject
from Explosion  import Explosion

from time import time
from math import sqrt
import pygame

START_X, START_Y = 200, 120

ACCEL_FACTOR = 40
SPEED_FACTOR = 20
MAX_SPEED    = 25

explosionSound = Resources.sounds['Explosion']

class Player(GameObject):
    def __init__(self):
        img = Resources.images['Spaceship']
        super().__init__(img, START_X, START_Y)

        self.posY  = START_Y
        self.velY  = 0.0
        self.acelY = 0.0

        self.score = 0
        self.alive = True
        self.explosion = None
    
    def draw(self):
        if self.alive:
            super().draw()
        elif self.explosion is not None:
            self.explosion.draw()
    
    def update(self, ts):
        if self.alive:
            if Util.is_key_pressed(pygame.K_SPACE):
                self.acelY = -1.0
            else:
                self.acelY = 0.8

            self.velY += ACCEL_FACTOR * self.acelY * ts
            self.velY = Util.clamp(self.velY, -MAX_SPEED, MAX_SPEED)
            dy = SPEED_FACTOR * self.velY * ts
            self.posY += dy
            print(self.posY)
            self.rect.centery = round(self.posY)
        
        elif self.explosion is not None:
            self.explosion.update(ts)
    
    def kill(self, explode=False):
        self.alive = False

        if explode:
            self.explosion = Explosion(self.rect.centerx, self.rect.centery)
            explosionSound.play()
    
    def in_bounds(self):
        return (-10 < self.rect.bottom) and (self.rect.top < Screen.HEIGHT)

    def get_score(self):
        return self.score
    
    def inc_score(self):
        self.score += 1
        return self.score
    
    def get_speed(self):
        return sqrt((self.score // 5) / 2) / 10 + 1
