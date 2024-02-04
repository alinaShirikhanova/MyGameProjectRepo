from random import randint

import pygame

from collectable.collectable import Collectable
from utils import load_image, WIDTH, HEIGHT

TO_GENERATE_COINS = pygame.USEREVENT + 2
class Coin(Collectable):
    def __init__(self, cost, pos, group):
        super().__init__(load_image('coin.png'), 1, 8, pos, group)
        self.cost = cost

    def collect(self, player):
        player.score += self.cost
        super().collect(player)









    @staticmethod
    def generate(n, group):
        for i in range(n):
            Coin(randint(1, 5),(randint(0, WIDTH), randint(0, HEIGHT)), group)








