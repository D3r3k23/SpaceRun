
import Screen
import Resources
import Util
from GameObject import GameObject
from Explosion import Explosion
from Exhaust import Exhaust

from time import time
from math import sqrt
import pygame

START_X, START_Y = 200, 120

ACCEL_FACTOR = 40
SPEED_FACTOR = 20
MAX_SPEED    = 25

img_normal = Resources.images['Spaceship']
img_thrust = Resources.images['Spaceship_turbo']

class Player(GameObject):
    SHOW_EXHAUST = True

    def __init__(self):
        super().__init__(img_normal, START_X, START_Y)

        self.posY  = START_Y
        self.velY  = 0.0

        self.score = 0
        self.alive = True
        self.explosion = None
        self.exhaust = Exhaust(self.rect)
    
    # Draw player or explosion
    def draw(self):
        if self.alive:
            super().draw()
            if Player.SHOW_EXHAUST:
                self.exhaust.draw()
        elif self.explosion is not None:
            self.explosion.draw()
    
    # Adjust acceleration based on Space Bar status, move player
    # If player dead: update explosion
    def update(self, ts):
        if self.alive:
            if Util.is_key_pressed(pygame.K_SPACE):
                acelY = -1.0
                self.img = img_thrust
            else:
                acelY = 0.8
                self.img = img_normal

            self.velY += ACCEL_FACTOR * acelY * ts
            self.velY = Util.clamp(self.velY, -MAX_SPEED, MAX_SPEED)
            dy = SPEED_FACTOR * self.velY * ts

            self.posY += dy
            self.rect.centery = round(self.posY)

            self.exhaust.update(ts, self.rect, self.get_speed())
        
        elif self.explosion is not None:
            self.explosion.update(ts)
    
    def kill(self, explode=False):
        self.alive = False

        if explode:
            self.explosion = Explosion(self.rect.centerx, self.rect.centery)
    
    def in_bounds(self):
        return (-10 < self.rect.bottom) and (self.rect.top < Screen.height())

    def get_score(self):
        return self.score
    
    def inc_score(self):
        self.score += 1
        return self.score
    
    def get_speed(self):
        return sqrt((self.score // 5) / 2) / 10 + 1
