
from GameObject import GameObject
import Resources

from collections import namedtuple
import random
import pygame

AsteroidSpec = namedtuple('AsteroidSpec', ['img', 'speed', 'size'])

asteroids = [
    AsteroidSpec(img = 'Asteroid1', speed = 12, size = (100, 89 )),
    AsteroidSpec(img = 'Asteroid2', speed = 18, size = (75,  66 )),
    AsteroidSpec(img = 'Asteroid3', speed = 15, size = (120, 120)),
    AsteroidSpec(img = 'Asteroid4', speed = 10, size = (160, 160))
]

SPEED_FACTOR  = 20
RAND_ROTATION = True

# Random choice of 4 asteroids
class Asteroid(GameObject):
    def __init__(self, screen, posY):
        spec = random.choice(asteroids)
        img = Resources.images[spec.img]

        img = pygame.transform.scale(img, spec.size)
        if RAND_ROTATION:
            angle = random.randint(0, 35) * 10
            img = pygame.transform.rotate(img, angle)

        self.posX = screen.get_width() + (img.get_width() / 2)

        super().__init__(screen, img, self.posX, posY)

        self.velX = spec.speed
        self.pastPlayer = False
        self.toDelete   = False
      
    def move(self, ts):
        self.posX -= SPEED_FACTOR * self.velX * ts
        self.rect.centerx = self.posX

        if self.pastPlayer:
            if self.posX < -(self.img.get_width() / 2):
                self.toDelete = True
    
    def pass_player(self):
        self.pastPlayer = True
