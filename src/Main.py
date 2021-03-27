
import Resources
import App

import os
import pygame

if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
    pygame.init()
    pygame.display.set_caption('Cave Run')
    screen = pygame.display.set_mode((1280, 720))
    
    Resources.load()
    App.run(screen)
