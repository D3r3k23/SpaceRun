
import Colors

import pygame

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def clear():
    screen.fill(Colors.BLACK)

def display():
    pygame.display.update()
    clear()

class Drawable:
    def __init__(self, img, x, y): # x, y: center coordinates
        width  = img.get_width()
        height = img.get_height()
        origin = (x - (width / 2), y - (height / 2))
    
        self.img  = img
        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self):
        screen.blit(self.img, self.rect)
