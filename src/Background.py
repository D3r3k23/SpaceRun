
import Screen
import Resources

from enum import Enum
from time import time
import pygame

SCROLL_SPEED = 20 # pix/sec
SCOLL_INT = 1 / SCROLL_SPEED

img = Resources.images['Background']

class Background:
    class Dir(Enum):
        NONE = 0
        DOWN = 1
        LEFT = 2

    def __init__(self, dir=0, speed=0):
        self.dir = dir
        self.set_speed(speed)

        self.lastScrollTime = time()
        self.dividerX = Screen.WIDTH
        self.dividerY = 0
    
    def set_speed(self, speed):
        self.scrollInt = 1 / speed

    def scroll(self):
        if self.dir == Background.Dir.DOWN:
            self.scroll_down()
        elif self.dir == Background.Dir.LEFT:
            self.scroll_left()

    def scroll_down(self):
        if time() - self.lastScrollTime >= self.scrollInt:
            self.lastScrollTime = time()
            self.dividerY += 1
            if self.dividerY == Screen.HEIGHT:
                self.dividerY = 0
    
    def scroll_left(self):
        if time() - self.lastScrollTime >= self.scrollInt:
            self.lastScrollTime = time()
            self.dividerX -= 1
            if self.dividerX == 0:
                self.dividerX = Screen.WIDTH

    def draw(self):
        if self.dir == Background.Dir.DOWN:
            origins = ((0, self.dividerY), (0, self.dividerY - Screen.HEIGHT))
        elif self.dir == Background.Dir.LEFT:
            origins = ((self.dividerX, 0), (self.dividerX - Screen.WIDTH, 0))
        else:
            origins = ((0, 0), (0, )) # no scrolling

        for origin in origins:
            Screen.draw_to_screen(img, pygame.Rect(origin, Screen.RES))
