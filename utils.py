import os
import sys

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 450

screen = pygame.display.set_mode(SIZE)
FPS = 30

def load_image(name, colorkey=None):
    fullname = os.path.join('data/sprites', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image