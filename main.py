import pygame as pg

from movable.enemy import TO_GENERATE_ENEMY, Enemy
from movable.player import Player
from utils import WIDTH, HEIGHT, screen, FPS

player_group = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player(10, (WIDTH // 2, HEIGHT // 2), player_group)
clock = pg.time.Clock()


pg.time.set_timer(TO_GENERATE_ENEMY, 4_000)

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        if e.type == TO_GENERATE_ENEMY:
            Enemy.generate(1, enemies)
    clock.tick(FPS)
    screen.fill('white')
    player_group.draw(screen)
    player_group.update()
    enemies.draw(screen)
    enemies.update(player)
    pg.display.update()

