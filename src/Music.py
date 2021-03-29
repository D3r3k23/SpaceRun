
from Util import *

import os.path
import random
import pygame

VOLUME_INIT = 0.2
VOLUME_STEP = 0.025
VOLUME_MAX  = 0.8

class Music():
    SONG_END = pygame.USEREVENT + 1

    def __init__(self):
        self.songs = []
        self.currentSong = None
        self.enabled = False
        
        pygame.mixer.music.set_endevent(Music.SONG_END)
    
    def add_song(self, fp):
        try:
            pygame.mixer.music.load(fp)
        except pygame.error:
            return

        self.songs.append(fp)
    
    def shuffle(self):
        random.shuffle(self.songs)
    
    def start(self):
        pygame.mixer.music.set_volume(VOLUME_INIT)

        if len(self.songs) > 0: # If any songs were loaded
            self.enabled = True
            self.currentSong = 0
            self.play_song()

    def next_song(self):
        if self.enabled:
            if self.currentSong == (len(self.songs) - 1):
                self.currentSong = 0
            else:
                self.currentSong += 1

            self.play_song()
    
    def prev_song(self):
        if self.enabled:
            if self.currentSong == 0:
                self.currentSong = (len(self.songs) - 1)
            else:
                self.currentSong -= 1
            
            self.play_song()
            
    def play_song(self):
        if self.enabled:
            pygame.mixer.music.load(self.songs[self.currentSong])
            pygame.mixer.music.play()
        
    def volume_up(self):
        vol = pygame.mixer.music.get_volume()
        newVol = clamp(vol + VOLUME_STEP, 0, VOLUME_MAX)
        pygame.mixer.music.set_volume(newVol)
        
    def volume_down(self):
        vol = pygame.mixer.music.get_volume()
        newVol = clamp(vol - VOLUME_STEP, 0, VOLUME_MAX)
        pygame.mixer.music.set_volume(newVol)
