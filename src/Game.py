
from Colors import *
#from Player import Player

import pygame
import time

running = False
score = 0
#player = Player()
asteroids = []

def play(screen):
    running = True
    prevTime = time.time()

    while running:
        newTime = time.time()
        ts = newTime - prevTime
        prevTime = newTime

        draw(screen)
        player.move(ts)
        collisions()
        events()

def draw(screen):
    screen.fill(BLACK) # Or space background

    for asteroid in asteroids:
        asteriod.draw(screen)
    
    player.draw(screen)

    # Draw score

    pygame.display.flip()

def collisions():
    pass
    
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
