
import Resources
import App

import os
import pygame

if __name__ == '__main__':
    # Setup Pygame
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
    pygame.init()
    pygame.display.set_caption('CaveRun')
    screen = pygame.display.set_mode((1280, 720))
    
    # Load resources and run app
    Resources.load()
    Resources.music.start()
    App.run(screen)
