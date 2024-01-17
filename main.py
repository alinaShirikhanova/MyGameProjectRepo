import sys

import pygame

from movable.player import Player
from utils import WIDTH, HEIGHT, screen

player_group = pygame.sprite.Group()
player = Player(10, (WIDTH // 2, HEIGHT // 2), player_group)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            # сразу будем завершать программу, чтобы не ломать переходы между сценами
            sys.exit()
    screen.fill('white')
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
