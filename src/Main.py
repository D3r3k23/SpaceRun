
import Resources
import App

import os
import random
import pygame

# Setup Pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
pygame.init()
pygame.display.set_caption('CaveRun')

random.seed()

# Load resources and run app
Resources.load()
Resources.music.start()
App.run()
App.exit()
