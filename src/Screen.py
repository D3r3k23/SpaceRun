
import Colors

import pygame

RES = WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode(RES)

def clear():
    screen.fill(Colors.BLACK)

def draw_background(img):
    draw_to_screen(img)

def draw_to_screen(img, rect=(0, 0)):
    screen.blit(img, rect)

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
        draw_to_screen(self.img, self.rect)
