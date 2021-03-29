
from Drawable import Drawable
import Resources

from collections import namedtuple
import random
import pygame

AsteroidSpec = namedtuple('AsteroidSpec', ['img', 'speed'])

asteroids = [
    AsteroidSpec(img = 'Asteroid1', speed = 8),
    AsteroidSpec(img = 'Asteroid2', speed = 12),
    AsteroidSpec(img = 'Asteroid3', speed = 15),
    AsteroidSpec(img = 'Asteroid4', speed = 5)
]

SPEED_FACTOR = 10

class Asteroid(Drawable):
    def __init__(self, screen):
        spec = random.choice(asteroids)
        img  = Resources.images[spec.img]

        x = screen.get_width() + img.get_width()
        y = random.randrange(screen.get_height())

        super().__init__(screen, img, x, y)

        self.speed = spec.speed
      
    def move(self, ts):
        pass      
