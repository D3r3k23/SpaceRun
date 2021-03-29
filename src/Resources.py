
from Music import Music

import os.path
import pygame

resource_dir = 'resources'

images = {}
sounds = {}
music = Music()

# Loads single image
def load_image(fn):
    fp = os.path.join(resource_dir, 'images', fn)
    try:
        surf = pygame.image.load(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load image: ' + fp)

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

# Loads single sound
def load_sound(fn):
    fp = os.path.join(resource_dir, 'sounds', fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load sound: ' + fp)
    
    return sound

def get_song_path(fn):
    return os.path.join(resource_dir, 'music', fn)

# Loads all resources
def load():
    # Images
    images['Play'       ] = load_image('play_button.png')
    images['Play_active'] = load_image('play_button_active.png')
    images['Exit'       ] = load_image('exit_button.png')
    images['Exit_active'] = load_image('exit_button_active.png')
    images['Spaceship'  ] = load_image('spaceship.png')
    images['Asteroid1'  ] = load_image('asteroid1.png')
    images['Asteroid2'  ] = load_image('asteroid2.png')
    images['Asteroid3'  ] = load_image('asteroid3.png')
    images['Asteroid4'  ] = load_image('asteroid4.png')

    # Sounds
    # sounds['PlayerDeath'] = load_sound('explosion1')

    # Music
    music.add_song(get_song_path('The Prototypes - Pale Blue Dot.ogg'))
    music.add_song(get_song_path('Teddy Killerz - Outer Space.ogg'))
    music.add_song(get_song_path('Phace & Misanthrop - Desert Orgy.ogg'))
    music.add_song(get_song_path('Mefjus & Break - Out Of Time.ogg'))
    music.add_song(get_song_path('Current Value - Dark Rain.ogg'))
    music.add_song(get_song_path('Noisia - Facade.ogg'))
    music.add_song(get_song_path('Fortran - Alien Girl.ogg'))
    music.add_song(get_song_path('Ed Rush & Optical - Mystery Machine.ogg'))
    music.add_song(get_song_path('Ed Rush & Optical - Fixation.ogg'))
    music.add_song(get_song_path('Andy C - Quest (Bladerunner Remix).ogg'))
    music.shuffle()
