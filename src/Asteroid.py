
import Screen
import Resources
from GameObject import GameObject

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

SPEED_FACTOR = 20
ROTATE_SPEED = 3 # Maybe make them spin as they move

# Random choice of 4 asteroids
class Asteroid(GameObject):
    RAND_ROTATION = True # Randomly rotates the images on init

    def __init__(self, posY):
        spec = random.choice(asteroids)
        img = Resources.images[spec.img]

        img = pygame.transform.scale(img, spec.size)
        if Asteroid.RAND_ROTATION:
            angle = random.randint(0, 35) * 10
            img = pygame.transform.rotate(img, angle)

        self.posX = Screen.WIDTH + (img.get_width() / 2)
        self.velX = spec.speed

        self.pastPlayer = False
        self.toDelete   = False

        super().__init__(img, self.posX, posY)
    
    # Moves asteroid based on player's speed, marks for deletion if past screen
    def update(self, ts, playerSpeed):
        dx = -(SPEED_FACTOR * playerSpeed * self.velX * ts)
        self.posX += dx
        self.rect.centerx = round(self.posX)

        if self.pastPlayer:
            if self.out_of_bounds():
                self.toDelete = True
    
    def pass_player(self):
        self.pastPlayer = True

    def out_of_bounds(self):
        return self.rect.right < 0
