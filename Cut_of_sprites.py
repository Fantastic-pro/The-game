import os
from Constants import *
import pygame
pygame.init()


size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
flag_of_game = False


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if colorkey is not None:
        image = pygame.image.load(fullname).convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        # Оставляем картинку прозрачной
        image = pygame.image.load(fullname).convert_alpha()
    return image


def load_sound(name):
    fullname = os.path.join('data', name)
    return fullname


pygame.init()
