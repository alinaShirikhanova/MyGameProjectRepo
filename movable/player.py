import pygame

from movable.movable import Movable
from utils import load_image


class Player(Movable):
    def __init__(self, speed, pos, group):
        super().__init__(speed, load_image('player.png'), 1,
                         6, pos, group)

    def update(self):
        pressed = pygame.key.get_pressed()
        controls = [pressed[pygame.K_w],
                    pressed[pygame.K_a],
                    pressed[pygame.K_s],
                    pressed[pygame.K_d]]
        if any(controls):
            self.move(*controls)

    def move(self, up, left, down, right):
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        if left:
            self.flip_left = True
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
        super().update()
