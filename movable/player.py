import pygame

from movable.movable import Movable
from utils import load_image


class Player(Movable):
    def __init__(self, speed, pos, group):
        super().__init__(speed, load_image('player.png'), 1,
                         6, pos, group)


    def update(self):
        pressed = pygame.key.get_pressed()
        controls = [pressed[pygame.K_UP], pressed[pygame.K_DOWN],
                    pressed[pygame.K_LEFT], pressed[pygame.K_RIGHT]]
        if any(controls):
            if pressed[pygame.K_UP]:
                self.rect.y -= self.speed
            if pressed[pygame.K_DOWN]:
                self.rect.y += self.speed
            if pressed[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if pressed[pygame.K_RIGHT]:
                self.rect.x += self.speed
            super().update()





