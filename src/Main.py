
import Resources
import App

import os
import random
import pygame

# Setup Pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
pygame.init()
pygame.display.set_caption('CaveRun')
screen = pygame.display.set_mode((1280, 720))

random.seed()

# Load resources and run app
Resources.load()
Resources.music.start()
App.run(screen)
App.exit()
