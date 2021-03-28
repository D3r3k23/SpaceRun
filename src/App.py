
import sys
import pygame

# App exit
def exit():
    pygame.quit()
    sys.exit()

# Handle app-level events, returns True if event handled
def handle_app_event(event):
    if event.type == pygame.QUIT:
        exit()
    
    elif event.type == Resources.Music.SONG_END:
        Resources.music.next_song()
        return True
    
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            Resources.music.next_song()
            return True
        
        elif event.key == pygame.K_LEFT:
            Resources.music.prev_song()
            return True
        
        elif event.key == pygame.K_UP:
            Resources.music.volume_up()
            return True
        
        elif event.key == pygame.K_DOWN:
            Resources.music.volume_down()
            return True

    return False # Event not handled
    

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
            if not handle_app_event(event):
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if startButton.contains(pos):
                        # Start button pressed
                        game = Game(screen)
                        exitCode = game.play()

                    elif exitButton.contains(pos):
                        # Exit button pressed
                        exit()

        screen.fill(BLACK)
        startButton.draw()
        exitButton.draw()
        pygame.display.flip()
