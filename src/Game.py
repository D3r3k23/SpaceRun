
import App
import Screen
import Resources
import Colors
import Util
from Text import Text
from Score import Score
from Player import Player
from Asteroid import Asteroid
from GameObject import GameObject
from Background import Background

from time import time
import random
import pygame

MAX_TS = 0.2

BACK_SPEED_START  = 150
BACK_SPEED_FACTOR = 100
background = Background(Background.Dir.LEFT, BACK_SPEED_START)
gameOverText = Text('GAME OVER!', 'SpaceSquadron', 64, Colors.RED, 640, 360)

thrustSound = Resources.sounds['Thrust']
thrustSoundChannel = pygame.mixer.Channel(0)
pygame.mixer.set_reserved(1)

class Game:
    def __init__(self):
        self.running = False
        self.paused  = False
        self.godMode = False

        self.scoreText = Score()
        self.player    = Player()

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
                self.player.update(ts)
                self.update_asteroids(ts)
                self.despawn_asteroids()
                
                if self.player.is_alive():
                    if self.check_asteroid_spawn(ts):
                        self.spawn_asteroid()
                
                background.scroll()
                if not self.godMode:
                    self.handle_collisions()
                self.render()
        
        pygame.mixer.stop()

    def render(self):
        background.draw()

        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.player.draw()

        self.scoreText.draw()
        if not self.player.is_alive():
            gameOverText.draw()
        
        Screen.display()

    def handle_events(self):
        for event in pygame.event.get():
            if App.handle_event(event):
                continue

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.player.is_alive():
                        self.toggle_paused()
                    else:
                        self.running = False
                
                elif event.key == pygame.K_c:
                    self.godMode = not self.godMode

                elif event.key == pygame.K_SPACE:
                    if not self.paused and self.player.is_alive():
                        thrustSoundChannel.play(thrustSound)
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    thrustSoundChannel.stop()
    
    def handle_collisions(self):
        if not self.player.in_bounds():
            self.game_over(crash=False)
        
        if self.player.is_alive():
            for asteroid in self.asteroids:
                if GameObject.collision(asteroid, self.player):
                    self.game_over(crash=True)
    
    def get_timestep(self):
        newFrameTime = time()
        ts = newFrameTime - self.prevFrameTime
        self.prevFrameTime = newFrameTime
        return min(ts, MAX_TS)
    
    def update_asteroids(self, ts):
        for asteroid in self.asteroids:
            asteroid.update(ts, self.player.get_speed())
            if not asteroid.pastPlayer and self.player.is_alive():
                if asteroid.rect.right < self.player.rect.left:
                    asteroid.pass_player()
                    score = self.player.inc_score()
                    self.scoreText.set_score(score)
                    background.set_speed(self.player.get_speed() * BACK_SPEED_FACTOR + (BACK_SPEED_START - BACK_SPEED_FACTOR))
        print('Player speed: ' + str(self.player.get_speed()))
        print('Scroll speed: ' + str(1 / background.scrollInt))
    
    def check_asteroid_spawn(self, ts):
        self.sinceLastSpawn += ts
        spawnInterval = 1.5 - ((self.asteroids[-1].velX - 8) / 10) - ((self.player.get_speed() - 1) * 1.2)
        spawnInterval = max(spawnInterval, 0.1)
        return self.sinceLastSpawn >= spawnInterval
    
    def spawn_asteroid(self):
        posY = random.randrange(Screen.HEIGHT - 50)
        asteroid = Asteroid(posY)
        self.asteroids.append(asteroid)
        self.sinceLastSpawn = 0.0

    def despawn_asteroids(self):
        self.asteroids[:] = [ a for a in self.asteroids if not a.toDelete ]
    
    def game_over(self, crash=False):
        self.player.kill(crash)
        thrustSoundChannel.stop()

    def pause(self):
        self.paused = True
        thrustSoundChannel.pause()
    
    def unpause(self):
        self.paused = False
        if Util.is_key_pressed(pygame.K_SPACE):
            thrustSoundChannel.unpause()
    
    def toggle_paused(self):
        if self.paused:
            self.unpause()
        else:
            self.pause()
