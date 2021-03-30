
import Resources

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
    

from Game import Game
from Menu import Menu

def run():
    Resources.music.start()
    running = True
    menu = Menu()

    while running:
        menu.run()
        choice = menu.get_choice()

        if choice == Menu.Choice.PLAY:
            game = Game()
            game.play()
        
        elif choice == Menu.Choice.EXIT:
            running = False
