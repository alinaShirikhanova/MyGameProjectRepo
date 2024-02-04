from random import randint

import pygame


from movable.movable import Movable
from utils import load_image, random_pos, WIDTH, HEIGHT

TO_GENERATE_ENEMY = pygame.USEREVENT + 7
class Enemy(Movable):
    def __init__(self, speed, pos, group):
        super().__init__(speed, load_image('enemy.png'), 1, 6, pos, group)
    def update(self, player):
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
            self.flip_left = True
        else:
            self.rect.x += self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        super().update()

    @staticmethod
    def generate(n, group):
        for i in range(n):
            Enemy(choice(Enemy.speeds), random_pos(), group)
