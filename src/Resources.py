
from Music import Music

import os.path
import pygame

resource_dir = 'resources'

images = {}
sounds = {}

music = Music()
fonts = {
    'SpaceSquadron': 'space_squadron.ttf'
}

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

def get_font_path(fn):
    return os.path.join(resource_dir, 'fonts', fn)

def load_font(name, size):
    if name == None:
        return pygame.font.SysFont(None, size)
    else:
        try:
            font = pygame.font.Font(get_font_path(fonts[name]), size)
        except (pygame.error, FileNotFoundError):
            return pygame.font.SysFont(None, size) # Default to pygame default font
        
        return font

# Loads all resources
def load():
    # Images

    images['Spaceship'  ] = load_image('spaceship.png')

    images['Play'       ] = load_image(os.path.join('buttons', 'play_button.png'))
    images['Play_active'] = load_image(os.path.join('buttons', 'play_button_active.png'))
    images['Exit'       ] = load_image(os.path.join('buttons', 'exit_button.png'))
    images['Exit_active'] = load_image(os.path.join('buttons', 'exit_button_active.png'))

    images['Asteroid1'] = load_image(os.path.join('asteroids', 'asteroid1.png'))
    images['Asteroid2'] = load_image(os.path.join('asteroids', 'asteroid2.png'))
    images['Asteroid3'] = load_image(os.path.join('asteroids', 'asteroid3.png'))
    images['Asteroid4'] = load_image(os.path.join('asteroids', 'asteroid4.png'))

    images['Explosion1' ] = load_image(os.path.join('explosion', 'explosion1.png'))
    images['Explosion2' ] = load_image(os.path.join('explosion', 'explosion2.png'))
    images['Explosion3' ] = load_image(os.path.join('explosion', 'explosion3.png'))
    images['Explosion4' ] = load_image(os.path.join('explosion', 'explosion4.png'))
    images['Explosion5' ] = load_image(os.path.join('explosion', 'explosion5.png'))
    images['Explosion6' ] = load_image(os.path.join('explosion', 'explosion6.png'))
    images['Explosion7' ] = load_image(os.path.join('explosion', 'explosion7.png'))
    images['Explosion8' ] = load_image(os.path.join('explosion', 'explosion8.png'))
    images['Explosion9' ] = load_image(os.path.join('explosion', 'explosion9.png'))
    images['Explosion10'] = load_image(os.path.join('explosion', 'explosion10.png'))
    images['Explosion11'] = load_image(os.path.join('explosion', 'explosion11.png'))

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
