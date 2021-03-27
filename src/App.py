
import sys
import pygame

# App exit
def exit():
    pygame.quit()
    sys.exit()

import Resources
from Game   import Game
from Button import Button
from Colors import *

# Runs the app menu
def run(screen):
    startButton = Button(screen, 640, 320, Resources.images['Start'])
    exitButton  = Button(screen, 640, 460, Resources.images['Exit'])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if startButton.contains(pos):
                    game = Game(screen)
                    exitCode = game.play()
                elif exitButton.contains(pos):
                    exit()

        screen.fill(BLACK)
        startButton.draw()
        exitButton.draw()
        pygame.display.flip()
