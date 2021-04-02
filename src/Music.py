
import Util

import random
import pygame

VOLUME_INIT = 0.25
VOLUME_STEP = 0.025
VOLUME_MAX  = 0.5

# Loads and plays music throughout application
class Music:
    EN_SHUFFLE = True
    SONG_END = pygame.USEREVENT + 1 # pygame.mixer.music song end event

    def __init__(self):
        self.songs = []
        self.currentSong = None
        self.enabled = False
        
        pygame.mixer.music.set_endevent(Music.SONG_END)
    
    # Add song to the queue
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

        if Music.EN_SHUFFLE:
            self.shuffle()

        if len(self.songs) > 0: # If any songs were loaded
            self.enabled = True
            self.currentSong = 0
            self.play_song()
    
    def stop(self):
        self.enabled = False
        pygame.mixer.music.stop()

    # Plays next song
    def next_song(self):
        if self.enabled:
            if self.currentSong == (len(self.songs) - 1):
                self.currentSong = 0
            else:
                self.currentSong += 1

            self.play_song()
    
    # Plays previous song
    def prev_song(self):
        if self.enabled:
            if self.currentSong == 0:
                self.currentSong = (len(self.songs) - 1)
            else:
                self.currentSong -= 1
            
            self.play_song()
    
    # Plays current song
    def play_song(self):
        if self.enabled:
            pygame.mixer.music.load(self.songs[self.currentSong])
            pygame.mixer.music.play()
        
    def volume_up(self):
        vol = pygame.mixer.music.get_volume()
        newVol = Util.clamp(vol + VOLUME_STEP, 0, VOLUME_MAX)
        pygame.mixer.music.set_volume(newVol)
        
    def volume_down(self):
        vol = pygame.mixer.music.get_volume()
        newVol = Util.clamp(vol - VOLUME_STEP, 0, VOLUME_MAX)
        pygame.mixer.music.set_volume(newVol)
