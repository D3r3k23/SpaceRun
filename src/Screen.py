
from Drawable import Drawable
import Colors
import Config

import pygame

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
items  = []

def clear():
    screen.fill(Colors.BLACK)

def draw(drawable):
    items.append(drawable)

def display():
    clear()    
    for item in items:
        item.draw(screen)
    items.clear()
    pygame.display.update()
