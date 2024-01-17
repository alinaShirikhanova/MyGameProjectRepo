import pygame

from animated_sprite import AnimatedSprite


class Movable(AnimatedSprite):
    def __init__(self, speed, sheet, rows, columns, pos, group):
        super().__init__(sheet, rows, columns, pos, group)
        self.speed = speed


    def update(self):
        super().update()

