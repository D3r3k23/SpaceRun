
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
    except (pygame.error, FileNotFoundError): # Error ????
        raise SystemExit(f'Could not load image: {fp}, {pygame.get_error}')

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

# Loads single sound
def load_sound(fn):
    fp = os.path.join(resource_dir, 'sounds', fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit(f'Could not load sound: {fp}, {pygame.get_error}')
    
    return sound

def get_song_path(fn):
    return os.path.join(resource_dir, 'music', fn)

# Loads all resources
def load():
    # Images
    images['Start'    ] = load_image('start_button.png')
    images['Exit'     ] = load_image('exit_button.png')
    images['Spaceship'] = load_image('spaceship.png')

    # Sounds
    # sounds['PlayerDeath'] = load_sound('explosion1')

    # Music
    music.add_song(get_song_path('The Prototypes - Pale Blue Dot.mp3'))
    music.add_song(get_song_path('Teddy Killerz - Outer Space.mp3'))
    music.add_song(get_song_path('Phace & Misanthrop - Desert Orgy.mp3'))
    music.add_song(get_song_path('Mefjus & Break - Out Of Time.mp3'))
    music.add_song(get_song_path('Current Value - Dark Rain.mp3'))
    music.add_song(get_song_path('Noisia - Facade.mp3'))
    music.add_song(get_song_path('Fortran - Alien Girl.mp3'))
    music.add_song(get_song_path('Ed Rush & Optical - Mystery Machine.mp3'))
    music.add_song(get_song_path('Ed Rush & Optical - Fixation.mp3'))
    music.add_song(get_song_path('Andy C - Quest (Bladerunner Remix).mp3'))
    music.shuffle()
