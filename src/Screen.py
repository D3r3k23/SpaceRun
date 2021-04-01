
import Colors

import pygame

RES = WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode(RES)

def clear():
    screen.fill(Colors.BLACK)

def draw_to_screen(img, rect=(0, 0)):
    screen.blit(img, rect)

def display():
    pygame.display.update()
    clear()

# Base class for drawable objects
# Created from image and coordinates, stores image and rect
class Drawable:
    def __init__(self, img, x, y, center=False): # x, y: center or (left, top) coordinates
        width  = img.get_width()
        height = img.get_height()
        if center:
            origin = (x - (width / 2), y - (height / 2))
        else:
            origin = (x, y)
    
        self.img  = img
        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self):
        draw_to_screen(self.img, self.rect)
