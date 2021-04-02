
import pygame

# Clamp number to range
def clamp(x, min_x, max_x):
    if x < min_x:
        return min_x
    elif x > max_x:
        return max_x
    else:
        return x

# key: pygame keycode
def is_key_pressed(key):
    return pygame.key.get_pressed()[key]

def get_mouse_pos():
    return pygame.mouse.get_pos()

def hide_mouse_on_hover():
    pygame.mouse.set_visible(False)

def show_mouse_on_hover():
    pygame.mouse.set_visible(True)
