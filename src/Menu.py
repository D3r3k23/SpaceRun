
from Button import Button
from Text   import Text
from Util   import *
from Colors import *
from App    import handle_app_event

from enum import Enum
import pygame

class Menu:
    class Choice(Enum):
        NONE = 0
        PLAY = 1
        EXIT = 2

    def __init__(self, screen):
        self.screen = screen
        self.playButton = Button(self.screen, 'Play', 540, 420)
        self.exitButton = Button(self.screen, 'Exit', 740, 420)
        self.title = Text(screen, 'Cave Run',
            'SpaceSquadron', 108, GREEN, 640, 250)
        
    # Runs the app menu
    def run(self):
        while True:
            self.handle_events()
            self.render()
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        return self.Choice.PLAY

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = get_mouse_pos()

                    if self.playButton.contains(pos):
                        return self.Choice.PLAY

                    elif self.exitButton.contains(pos):
                        return self.Choice.EXIT

    def render(self):
        self.screen.fill(BLACK)

        self.playButton.draw()
        self.exitButton.draw()
        self.title.draw()

        pygame.display.flip()
