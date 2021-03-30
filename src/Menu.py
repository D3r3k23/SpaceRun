
from App    import handle_app_event
from Button import Button
from Text   import Text
import Screen
import Util
import Colors

from enum import Enum
import pygame

titleText = Text('Cave Run', 'SpaceSquadron', 108, Colors.GREEN, 640, 250)
playButton = Button('Play', 540, 420)
exitButton = Button('Exit', 740, 420)

class Menu:
    class Choice(Enum):
        NONE = 0
        PLAY = 1
        EXIT = 2
    
    def __init__(self):
        self.running = False
        self.choice = Menu.Choice.NONE
        
    # Runs the app menu
    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.render()

    def render(self):
        titleText.draw()
        playButton.draw()
        exitButton.draw()

        Screen.display()
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.choose_item(Menu.Choice.PLAY)

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = Util.get_mouse_pos()

                    if playButton.contains(pos):
                        self.choose_item(Menu.Choice.PLAY)

                    elif exitButton.contains(pos):
                        self.choose_item(Menu.Choice.EXIT)

    def choose_item(self, choice):
        self.choice = choice
        self.running = False

    def get_choice(self):
        return self.choice
