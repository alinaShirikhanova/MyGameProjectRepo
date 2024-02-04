import pygame.mixer

from animated_sprite import AnimatedSprite


class Collectable(AnimatedSprite):
    def __init__(self, sheet, rows, columns, pos, group):
        super().__init__(sheet, rows, columns, pos, group)
        self.sound = pygame.mixer.Sound('data/sounds/default_collectable.wav')

    def collect(self, player):
        self.sound.play()
        self.kill()







