
import pygame
import os.path

main_dir = os.path.split(os.path.abspath(__file))[0]
src_dir  = os.path.join(main_dir, 'resources')

images = {}
sounds = {}

def load_image(fn):
    fp = os.path.join(src_dir, fn)
    try:
        surf = pygame.image.load(fp)
    except pygame.error:
        raise SystemExit(f'Could not load image: {fp}, {pygame.get_error}')
    return surf.convert()

def load_sound(fn):
    fp = os.path.join(src_dir, fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except pygame.error:
        raise SystemExit(f'Could not load sound: {fp}, {pygame.get_error}')
    return sound

def load_resources():
    images['Player'] = load_image('spaceship.png')

    # sounds['PlayerDeath'] = load_sound('explosion1')
