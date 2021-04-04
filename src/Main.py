
import random
random.seed()

#-------- Pygame setup --------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame
pygame.init()

#-------- User setup --------#

import App
App.set_caption('Space Run')
App.set_icon('icon.png')

import Screen
Screen.init(1280, 720)

import Resources
Resources.load()

#-------- Run app --------#

from Menu import Menu
from Game import Game

menu = Menu()
Resources.music.start()

while True:
    choice = menu.run()
    if choice == Menu.Choice.PLAY:
        game = Game()
        game.play()
    elif choice == Menu.Choice.EXIT:
        App.exit()
