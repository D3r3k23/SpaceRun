
from Colors   import *
from Player   import Player
from Asteroid import Asteroid
from App      import exit, handle_app_event

from time import time
import pygame

class Game:
    def __init__(self, screen):
        self.screen  = screen
        self.running = False
        self.paused  = False

        self.player = Player(screen)
        self.score  = 0

        self.asteroids = []
        self.prevFrameTime = 0

    def play(self):
        self.running = True
        self.prevFrameTime = time()

        while self.running:
            ts = self.get_timestep()

            if not self.paused:
                self.player.move(ts)

                for asteroid in self.asteroids:
                    asteroid.move(ts)
                
                self.handle_collisions()

                self.handle_events()
                
                self.draw()
    
    def get_timestep(self):
        newFrameTime = time()
        ts = newFrameTime - self.prevFrameTime
        self.prevFrameTime = newFrameTime
        return ts

    def draw(self):
        self.screen.fill(BLACK) # Or space background

        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.player.draw()

        # Draw score

        pygame.display.flip()

    def handle_collisions(self):
        if not self.player.in_bounds():
            self.running = False
        
        for asteroid in self.asteroids:
            if asteroid.rect.colliderect(self.player.rect):
                self.running = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.paused:
                            self.unpause()
                        else:
                            self.pause()
    
    def pause(self):
        self.paused = True
    
    def unpause(self):
        self.paused = False
