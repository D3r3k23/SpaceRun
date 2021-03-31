
import App
import Screen
import Resources
import Colors
import Util
import Config
from Text       import Text
from Score      import Score
from Player     import Player
from Asteroid   import Asteroid
from GameObject import GameObject

from time import time
import random
import pygame

ASTEROID_SPAWN_INT = 2

gameOverText = Text('GAME OVER!', 'SpaceSquadron', 64, Colors.RED, 640, 360)

class Game:
    def __init__(self):
        self.running = False
        self.paused  = False

        self.scoreText = Score()
        self.player = Player()

        self.asteroids = []
        self.sinceLastSpawn = 0.0
        self.prevFrameTime = 0

    def play(self):
        self.running = True
        self.prevFrameTime = time()
        self.spawn_asteroid()

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

    def render(self):
        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.player.draw()

        self.scoreText.draw()
        if not self.player.is_alive():
            gameOverText.draw()
        
        Screen.display()

    def handle_events(self):
        for event in pygame.event.get():
            if not App.handle_event(event):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.player.is_alive():
                            self.toggle_paused()
                        else:
                            self.running = False
    
    def handle_collisions(self):
        if not self.player.in_bounds():
            self.player.kill()
        
        for asteroid in self.asteroids:
            if GameObject.collision(asteroid, self.player):
                self.player.kill(explode=True)
    
    def get_timestep(self):
        newFrameTime = time()
        ts = newFrameTime - self.prevFrameTime
        self.prevFrameTime = newFrameTime
        return ts
    
    def move_asteroids(self, ts):
        for asteroid in self.asteroids:
            asteroid.move(ts)
            if not asteroid.pastPlayer and self.player.is_alive():
                if asteroid.rect.right < self.player.rect.left:
                    asteroid.pass_player()
                    self.player.inc_score()
                    self.scoreText.set_score(self.player.get_score())
    
    def check_asteroid_spawn(self, ts):
        self.sinceLastSpawn += ts
        return self.sinceLastSpawn >= ASTEROID_SPAWN_INT
    
    def spawn_asteroid(self):
        posY = random.randrange(Config.SCREEN_HEIGHT - 50)
        asteroid = Asteroid(posY)
        self.asteroids.append(asteroid)
        self.sinceLastSpawn = 0.0

    def despawn_asteroids(self):
        self.asteroids[:] = [ a for a in self.asteroids if not a.toDelete ]

    def pause(self):
        self.paused = True
    
    def unpause(self):
        self.paused = False
    
    def toggle_paused(self):
        self.paused = not self.paused
