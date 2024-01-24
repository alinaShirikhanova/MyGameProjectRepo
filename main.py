from random import randint

import pygame as pg

from movable.enemy import Enemy
from movable.player import Player
from utils import WIDTH, HEIGHT, screen, FPS

player_group = pg.sprite.Group()
player = Player(10, (WIDTH // 2, HEIGHT // 2), player_group)

enemies = pg.sprite.Group() # 2-ое задание
enemy = Enemy(8,  (randint(0, WIDTH), randint(0, HEIGHT)), enemies)

clock = pg.time.Clock()

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    clock.tick(FPS)
    screen.fill('white')


    player_group.draw(screen)
    player_group.update()

    enemies.draw(screen)
    enemies.update(player)

    pg.display.update()

