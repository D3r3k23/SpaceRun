#!/usr/bin/env python3

import Game
import pygame

def quit():
    pygame.quit()
    sys.exit()

def run():
    screen = pygame.display.set_mode((1280, 720))

    # Menu

    startButton
    quitButton

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if startButton clicked:
                    Game.play(screen)
                elif quitButton clicked:
                    quit()

if __name__ == "__main__":
    pygame.init()
    run()
