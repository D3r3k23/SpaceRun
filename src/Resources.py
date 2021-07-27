
from Music import Music

import os
import pygame

resource_dir = 'resources'

images = {} # Name: pygame.Surface
sounds = {} # Name: pygame.mixer.Sound

music = Music()
fonts = {} # Name: file-path

# Loads all resources
def load():
    load_images()
    load_sounds()
    load_music()
    load_fonts()

def get_image_path(folder, fn):
    return os.path.join(resource_dir, 'images', folder, fn)

def get_sound_path(fn):
    return os.path.join(resource_dir, 'sounds', fn)

def get_song_path(fn):
    return os.path.join(resource_dir, 'music', fn)

def get_font_path(fn):
    return os.path.join(resource_dir, 'fonts', fn)

def load_image(folder, fn):
    fp = get_image_path(folder, fn)
    try:
        surf = pygame.image.load(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load image: ' + fp)

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

def load_sound(fn, vol):
    fp = get_sound_path(fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit('Could not load sound: ' + fp)
    
    sound.set_volume(vol)
    return sound

def load_font(font, size): # Font name | Size in pixels
    try:
        return pygame.font.Font(fonts[font], size)
    except (pygame.error, FileNotFoundError):
        return pygame.font.SysFont(None, size) # Default to pygame default fonts

def load_images():
    images['Background'] = load_image('background', 'starfield.png')

    images['Spaceship'      ] = load_image('spaceship', 'spaceship.png')
    images['Spaceship_turbo'] = load_image('spaceship', 'spaceship_turbo.png', )

    images['Exhaust'] = [ # Animation
        load_image('spaceship', 'exhaust1.png'),
        load_image('spaceship', 'exhaust2.png'),
        load_image('spaceship', 'exhaust3.png'),
        load_image('spaceship', 'exhaust4.png')
    ]

    images['Play'       ] = load_image('buttons', 'play_button.png')
    images['Play_active'] = load_image('buttons', 'play_button_active.png')
    images['Exit'       ] = load_image('buttons', 'exit_button.png')
    images['Exit_active'] = load_image('buttons', 'exit_button_active.png')

    images['Asteroid1'] = load_image('asteroids', 'asteroid1.png')
    images['Asteroid2'] = load_image('asteroids', 'asteroid2.png')
    images['Asteroid3'] = load_image('asteroids', 'asteroid3.png')
    images['Asteroid4'] = load_image('asteroids', 'asteroid4.png')

    images['Explosion'] = [ # Animation
        load_image('explosion', 'explosion1.png'),
        load_image('explosion', 'explosion2.png'),
        load_image('explosion', 'explosion3.png'),
        load_image('explosion', 'explosion4.png'),
        load_image('explosion', 'explosion5.png'),
        load_image('explosion', 'explosion6.png'),
        load_image('explosion', 'explosion7.png'),
        load_image('explosion', 'explosion8.png'),
        load_image('explosion', 'explosion9.png'),
        load_image('explosion', 'explosion10.png'),
        load_image('explosion', 'explosion11.png')
    ]

def load_sounds():
    sounds['Explosion'] = load_sound('crash_explosion.ogg',  0.4)
    sounds['Thrust'   ] = load_sound('spaceship_thrust.ogg', 0.5)
    
    # Reserve channel for thrust sound (channel 0)
    pygame.mixer.set_reserved(1)

def load_music():
    for song in os.listdir(os.path.join('resources', 'music')):
        music.add_song(get_song_path(song))

def load_fonts():
    fonts['SpaceSquadron'] = get_font_path('space_squadron.ttf')
