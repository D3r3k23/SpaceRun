
import Screen
import Resources

from enum import Enum
from time import time
import pygame

img = pygame.transform.scale(Resources.images['Background'], Screen.res())

class Background:
    class ScrollDir(Enum):
        NONE = 0
        DOWN = 1
        LEFT = 2

    def __init__(self, dir=0, speed=0): # Speed: pix/s
        self.dir = dir
        self.set_speed(speed)

        self.lastScrollTime = time()
        self.dividerX = Screen.width()
        self.dividerY = 0
    
    def set_speed(self, speed):
        self.scrollInt = 1 / speed

    def scroll(self):
        if self.dir == Background.ScrollDir.DOWN:
            self.scroll_down()
        elif self.dir == Background.ScrollDir.LEFT:
            self.scroll_left()

    def scroll_down(self):
        if time() - self.lastScrollTime >= self.scrollInt:
            self.lastScrollTime = time()
            self.dividerY += 1
            if self.dividerY == Screen.height():
                self.dividerY = 0
    
    def scroll_left(self):
        if time() - self.lastScrollTime >= self.scrollInt:
            self.lastScrollTime = time()
            self.dividerX -= 1
            if self.dividerX == 0:
                self.dividerX = Screen.width()

    def draw(self):
        if self.dir == Background.ScrollDir.DOWN:
            origins = ((0, self.dividerY), (0, self.dividerY - Screen.height()))
        elif self.dir == Background.ScrollDir.LEFT:
            origins = ((self.dividerX, 0), (self.dividerX - Screen.width(), 0))
        else:
            origins = ((0, 0), (0, 0)) # no scrolling

        for origin in origins:
            Screen.draw_to_screen(img, pygame.Rect(origin, Screen.res()))
