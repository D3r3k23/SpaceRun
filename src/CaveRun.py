#!/usr/bin/env python3

import Resources

from Button import Button
from Colors import *
import Game

import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

import pygame

def exit():
    pygame.quit()
    sys.exit()

def run():
    screen = pygame.display.set_mode((1280, 720))
    Resources.load()

    #----- Menu -----#

    start = Button(640, 320, Resources.images['Start'])
    exit  = Button(640, 460, Resources.images['Exit'])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if start.contains(pos):
                   Game.play(screen)
                elif exit.contains(pos):
                   exit()

        screen.fill(BLACK)
        start.draw(screen)
        exit.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    run()
