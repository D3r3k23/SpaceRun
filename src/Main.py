
import random
random.seed()

#-------- Pygame setup --------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame
pygame.init()
pygame.display.set_caption('SpaceRun')

#-------- User setup --------#

import Screen
Screen.init(1280, 720)

import Resources
Resources.load()

#-------- Run app --------#

import App
from Menu import Menu
from Game import Game

Resources.music.start()
menu = Menu()

while True:
    choice = menu.run()
    if choice == Menu.Choice.PLAY:
        game = Game()
        game.play()
    
    elif choice == Menu.Choice.EXIT:
        App.exit()
