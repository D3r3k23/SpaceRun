#!/usr/bin/env python3

from Button import Button
from Colors import *
import Game
import Resources

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame

def quit():
    pygame.quit()
    sys.exit()

def run():
    screen = pygame.display.set_mode((1280, 720))
    Resources.load()


    ##### Menu ####

    start = Button(640, 360, 80, 30, BLUE, WHITE, 'Corbel', 25, 'Start')
    quit  = Button(640, 275, 80, 30, RED,  WHITE, 'Corbel', 15, 'Quit' )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #if startButton clicked:
                #    Game.play(screen)
                #elif quitButton clicked:
                #    quit()

if __name__ == "__main__":
    pygame.init()
    run()
