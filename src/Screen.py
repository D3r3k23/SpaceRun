
import Resources
import Colors

import pygame

screen = None

def init(width, height):
    global screen
    set_caption('SpaceRun')
    set_icon('icon.png')
    screen = pygame.display.set_mode((width, height))

def set_caption(caption):
    pygame.display.set_caption(caption)

def set_icon(fn):
    icon = pygame.image.load(Resources.get_image_path('icon', fn))
    pygame.display.set_icon(icon)

def width():
    return screen.get_width()

def height():
    return screen.get_height()

def res():
    return (screen.get_width(), screen.get_height())

def rect():
    return screen.get_rect()

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
        origin = (x - (width // 2), y - (height // 2)) if center else (x, y)
    
        self.img  = img
        self.rect = pygame.Rect(origin, (width, height))
    
    def draw(self):
        draw_to_screen(self.img, self.rect)
