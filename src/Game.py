
import Resources
from Colors   import *
from Util     import *
from Score    import Score
from GameOver import GameOver
from Player   import Player
from Asteroid import Asteroid
from App      import handle_app_event

from time import time
import pygame

ASTEROID_SPAWN_INT = 2

class Game:
    def __init__(self, screen):
        self.screen   = screen
        self.running  = False
        self.paused   = False

        self.player = Player(screen)
        self.score  = Score(screen)
        self.gameOverText = GameOver(screen)

        self.asteroids = []
        self.sinceLastSpawn = 0.0
        self.prevFrameTime = 0

    def play(self):
        self.running = True
        self.prevFrameTime = time()

        while self.running:
            ts = self.get_timestep()
            self.handle_events()

            if not self.paused:
                self.player.move(ts)
                self.move_asteroids(ts)
                self.despawn_asteroids()
                
                if self.player.is_alive():
                    if self.check_asteroid_spawn(ts):
                        self.spawn_asteroid()
                
                self.handle_collisions()
                self.render()
    
    def get_timestep(self):
        newFrameTime = time()
        ts = newFrameTime - self.prevFrameTime
        self.prevFrameTime = newFrameTime
        return ts

    def render(self):
        self.screen.fill(BLACK) # Or space background

        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.player.draw()
        self.score.draw()
        if not self.player.is_alive():
            self.gameOverText.draw()
        
        pygame.display.flip()
    
    def move_asteroids(self, ts):
        for asteroid in self.asteroids:
            asteroid.move(ts)
            if not asteroid.pastPlayer and self.player.is_alive():
                if asteroid.rect.right < self.player.rect.left:
                    asteroid.pass_player()
                    self.player.inc_score()
                    self.score.update(self.player.get_score())
    
    def check_asteroid_spawn(self, ts):
        self.sinceLastSpawn += ts
        return self.sinceLastSpawn >= ASTEROID_SPAWN_INT
    
    def spawn_asteroid(self):
        asteroid = Asteroid(self.screen)
        self.asteroids.append(asteroid)
        self.sinceLastSpawn = 0.0

    def despawn_asteroids(self):
        self.asteroids[:] = [ a for a in self.asteroids if not a.toDelete ]

    def handle_collisions(self):
        if not self.player.in_bounds():
            self.game_over()
        
        for asteroid in self.asteroids:
            if asteroid.rect.colliderect(self.player.rect):
                self.game_over()
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.player.is_alive():
                            self.toggle_paused()
                        
                        else:
                            self.running = False
    
    def game_over(self):
        self.player.kill()
    
    def pause(self):
        self.paused = True
    
    def unpause(self):
        self.paused = False
    
    def toggle_paused(self):
        self.paused = not self.paused
