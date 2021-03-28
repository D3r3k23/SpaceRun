
from Drawable import Drawable
import Resources
from Util import *

import time
import pygame

ACCEL_FACTOR = 25
SPEED_FACTOR = 40

MAX_SPEED = 10

class Player(Drawable):
    def __init__(self, screen):
        img    = Resources.images['Spaceship']
        width  = img.get_width()
        height = img.get_height()

        x, y = 200, 120 # Starting position
        origin = (x - (width / 2), y - (height / 2))
        rect   = pygame.Rect(origin, (width, height))

        self.posY  = y
        self.velY  = 0.0
        self.acelY = 0.0

        self.alive = True

        super().__init__(screen, img, rect)
    
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
        self.timeOfDeath = time.time()
    
    def is_alive(self):
        return self.alive
    
    def in_bounds(self):
        return (-20 < self.rect.bottom) and (self.rect.top < self.screen.get_height())
