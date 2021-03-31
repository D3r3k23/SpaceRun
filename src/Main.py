
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
