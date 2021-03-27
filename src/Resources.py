
import os.path
import pygame

resource_dir = 'resources'

images = {}
sounds = {}

# Loads single image
def load_image(fn):
    fp = os.path.join(resource_dir, fn)
    try:
        surf = pygame.image.load(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit(f'Could not load image: {fp}, {pygame.get_error}')

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

# Loads single sound
def load_sound(fn):
    fp = os.path.join(src_dir, fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit(f'Could not load sound: {fp}, {pygame.get_error}')
    
    return sound

# Loads all resources
def load():
    images['Start'    ] = load_image('start_button.png')
    images['Exit'     ] = load_image('exit_button.png')
    images['Spaceship'] = load_image('spaceship.png')

    # sounds['PlayerDeath'] = load_sound('explosion1')
