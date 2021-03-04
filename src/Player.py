
from Resources import images
from Resources import sounds

import pygame

SPEED = 5

class Player:
    def __init__(self):
        self.sprite = images[Player]
        self.rect = sprite.get_rect()

        self.posX = 20
        self.posY = 360

        self.velX = 0.0
        self.velY = 0.0
    
    def move(self, ts):
        if pygame.key.get_pressed()[K_SPACE]:
            self.velY = 1.0
        else:
            self.velY = -1.0
        
        self.posY += int(SPEED * velY * ts)
        self.rect.center = (posX, posY)
    
    def draw(self, screen):
        screen.blit(sprite, rect)

# acelY = 1.0, -1.0
# ts: velY += acelY
