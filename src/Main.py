
import random
random.seed()

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame
pygame.init()
pygame.display.set_caption('SpaceRun')

import Screen
import Resources
Resources.load()

import App
App.run()
App.exit()
