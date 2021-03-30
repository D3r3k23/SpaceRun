
from App    import handle_app_event
from Button import Button
from Text   import Text
import Screen
import Util
import Colors

from enum import Enum
import pygame

class Menu:
    class Choice(Enum):
        NONE = 0
        PLAY = 1
        EXIT = 2
    
    def __init__(self):
        self.running = False
        self.choice = Menu.Choice.NONE

        self.titleText = Text('Cave Run', 'SpaceSquadron', 108, Colors.GREEN, 640, 250)
        self.playButton = Button('Play', 540, 420)
        self.exitButton = Button('Exit', 740, 420)
        
    # Runs the app menu
    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.render()
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.choose_item(Menu.Choice.PLAY)

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = Util.get_mouse_pos()

                    if self.playButton.contains(pos):
                        self.choose_item(Menu.Choice.PLAY)

                    elif self.exitButton.contains(pos):
                        self.choose_item(Menu.Choice.EXIT)

    def choose_item(self, choice):
        self.choice = choice
        self.running = False

    def render(self):
        Screen.draw(self.titleText)
        Screen.draw(self.playButton)
        Screen.draw(self.exitButton)

        Screen.display()

    def get_choice(self):
        return self.choice
