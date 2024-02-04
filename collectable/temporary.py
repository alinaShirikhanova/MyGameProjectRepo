import pygame.time

from collectable.collectable import Collectable


class Temporary(Collectable):
    def __init__(self, sheet, rows, columns, pos, group, ttl_ms=5000):
        super().__init__(sheet, rows, columns, pos, group)
        self.ttl = ttl_ms
        self.time_created = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if self.ttl <= now - self.time_created:
            self.kill()
        super().update()
