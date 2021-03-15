
import Resources

import pygame

SPEED = 75

class Player:
    def __init__(self):
        image  = Resources.images['Spaceship']
        width  = image.get_width()
        height = image.get_height()

        x = 200
        y = 360
        origin = (x - (width / 2), y - (height / 2))

        self.posY  = y
        self.velY  = 0.0
        self.image = image
        self.rect  = pygame.Rect(origin, (width, height))
    
    def move(self, ts):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.velY = -1.0
        else:
            self.velY = 1.0

        self.posY += SPEED * self.velY * ts
        self.rect.centery = self.posY

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# acelY = 1.0, -1.0
# ts: velY += acelY
