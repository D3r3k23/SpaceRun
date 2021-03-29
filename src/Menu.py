
from Button import Button
from Util   import *
from Colors import *
from App    import handle_app_event

from enum import Enum
import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.playButton = Button(self.screen, 'Play', 490, 360)
        self.exitButton = Button(self.screen, 'Exit', 790, 360)

    class Choice(Enum):
        NONE = 0
        PLAY = 1
        EXIT = 2

# Runs the app menu
    def run(self):
        while True:
            for event in pygame.event.get():
                if not handle_app_event(event):
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = get_mouse_pos()

                        if self.playButton.contains(pos):
                            return self.Choice.PLAY

                        elif self.exitButton.contains(pos):
                            return self.Choice.EXIT

            self.screen.fill(BLACK)
            self.playButton.draw()
            self.exitButton.draw()
            pygame.display.flip()
