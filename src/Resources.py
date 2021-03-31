
from Music import Music

import os.path
import pygame

resource_dir = 'resources'

images = {}
sounds = {}

music = Music()
fonts = {}

# Loads single image
def load_image(folder, fn):
    fp = os.path.join(resource_dir, 'images', folder, fn)
    try:
        surf = pygame.image.load(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load image: ' + fp)

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

# Loads single sound
def load_sound(fn, vol):
    fp = os.path.join(resource_dir, 'sounds', fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load sound: ' + fp)
    
    sound.set_volume(vol)
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
            font = pygame.font.Font(fonts[name], size)
        except (pygame.error, FileNotFoundError):
            return pygame.font.SysFont(None, size) # Default to pygame default font
        
        return font

def load():
    load_images()
    load_sounds()
    load_music()
    load_fonts()

def load_images():
    images['Spaceship'] = load_image('spaceship', 'spaceship.png')
    images['Exhaust1' ] = load_image('spaceship', 'exhaust1.png')
    images['Exhaust2' ] = load_image('spaceship', 'exhaust2.png')
    images['Exhaust3' ] = load_image('spaceship', 'exhaust3.png')
    images['Exhaust4' ] = load_image('spaceship', 'exhaust4.png')

    images['Play'       ] = load_image('buttons', 'play_button.png')
    images['Play_active'] = load_image('buttons', 'play_button_active.png')
    images['Exit'       ] = load_image('buttons', 'exit_button.png')
    images['Exit_active'] = load_image('buttons', 'exit_button_active.png')

    images['Asteroid1'] = load_image('asteroids', 'asteroid1.png')
    images['Asteroid2'] = load_image('asteroids', 'asteroid2.png')
    images['Asteroid3'] = load_image('asteroids', 'asteroid3.png')
    images['Asteroid4'] = load_image('asteroids', 'asteroid4.png')

    images['Explosion1' ] = load_image('explosion', 'explosion1.png')
    images['Explosion2' ] = load_image('explosion', 'explosion2.png')
    images['Explosion3' ] = load_image('explosion', 'explosion3.png')
    images['Explosion4' ] = load_image('explosion', 'explosion4.png')
    images['Explosion5' ] = load_image('explosion', 'explosion5.png')
    images['Explosion6' ] = load_image('explosion', 'explosion6.png')
    images['Explosion7' ] = load_image('explosion', 'explosion7.png')
    images['Explosion8' ] = load_image('explosion', 'explosion8.png')
    images['Explosion9' ] = load_image('explosion', 'explosion9.png')
    images['Explosion10'] = load_image('explosion', 'explosion10.png')
    images['Explosion11'] = load_image('explosion', 'explosion11.png')

def load_sounds():
    sounds['Explosion'] = load_sound('crash_explosion.wav', 0.1)
    sounds['Thrust'   ] = load_sound('spaceship_thrust.wav', 0.05)

def load_music():
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

def load_fonts():
    fonts['SpaceSquadron'] = get_font_path('space_squadron.ttf')
