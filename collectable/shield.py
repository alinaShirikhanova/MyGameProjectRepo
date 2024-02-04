from random import randint

import pygame

from collectable.temporary import Temporary
from utils import load_image, WIDTH, HEIGHT

TO_GENERATE_SHIELD = pygame.USEREVENT + 4
TO_LOSE_SHIELD = pygame.USEREVENT + 5


class Shield(Temporary):
    def __init__(self, pos, group, time=5_000):
        super().__init__(load_image('shield.gif', -1), 1, 8, pos, group)
        self.sound = pygame.mixer.Sound('data/sounds/shield.wav')
        self.time = time

    def collect(self, player):
        # когда игрок подбирает щит - поднимается соответствующий флаг-атрибут
        player.protected = True
        # Создадим событие потери щита через n миллисекунд без повторений
        pygame.time.set_timer(TO_LOSE_SHIELD, self.time, 1)
        super().collect(player)

    @staticmethod
    def generate(n, group):
        for i in range(n):
            Shield((randint(0, WIDTH), randint(0, HEIGHT)), group)
