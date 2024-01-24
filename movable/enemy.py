from movable.movable import Movable
from utils import load_image


class Enemy(Movable):
    def __init__(self, speed, pos, group):
        super().__init__(speed, load_image('enemy.png'), 1, 6, pos, group)

    def update(self, player):
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed
        if player.rect.x > self.rect.x:
            self.rect.x += self.speed
        if player.rect.y > self.rect.y:
            self.rect.y += self.speed
        super().update()


        # Задание
        # Дописать эту часть кода и дописать оставшиея 3 случая


# 1. Реализовать поворот противника
# 2. В основной программе создать группу для противников
# 3. В основной программе создать одного противника
# 5. В основной программе в цикле отрисовать группу противников
# 6. В основной программе в цикле вызвать функию update у группы противников
