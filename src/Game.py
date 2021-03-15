
from Colors  import *
from Player  import Player
from CaveRun import exit

import pygame
import time

def play(screen):
    running = True
    score = 0
    player = Player()
    asteroids = []

    prevTime = time.time()
    
    while running:
        newTime = time.time()
        ts = newTime - prevTime
        prevTime = newTime

        events()
        
        player.move(ts)
        for asteroid in asteroids:
            asteroid.move(ts)
        
        collisions()
        
        draw(screen, player, asteroids)

def draw(screen, player, asteroids):
    screen.fill(BLACK) # Or space background

    for asteroid in asteroids:
        asteroid.draw(screen)
    
    player.draw(screen)

    # Draw score

    pygame.display.flip()

def collisions():
    pass
    
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
