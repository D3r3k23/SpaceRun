
import random
random.seed()

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame
pygame.init()
pygame.display.set_caption('CaveRun')

import Resources
import App

Resources.load()
App.run()
App.exit()
