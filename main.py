from random import randint

import pygame as pg
from pygame.mixer import music

from collectable.coin import TO_GENERATE_COINS, Coin
from collectable.shield import TO_GENERATE_SHIELD, Shield, TO_LOSE_SHIELD
from movable.enemy import Enemy, TO_GENERATE_ENEMY
from movable.player import Player
from utils import WIDTH, HEIGHT, screen, FPS, font

player_group = pg.sprite.Group()
collectables = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player(10, (WIDTH // 2, HEIGHT // 2), player_group)
enemy = Enemy(6,  (randint(0, WIDTH), randint(0, HEIGHT)), enemies)
clock = pg.time.Clock()
pg.time.set_timer(TO_GENERATE_ENEMY, 4000)
pg.time.set_timer(TO_GENERATE_COINS, 3000)
pg.time.set_timer(TO_GENERATE_SHIELD, 2000)


music.load('data/sounds/battle1.mp3')
music.set_volume(0.1)
music.play(-1)
start_frame = font.render('CATCH IF YOU CAN', True, 'blue')

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    screen.fill('white')
    pg.display.update()


running = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        if e.type == TO_GENERATE_ENEMY:
            Enemy.generate(enemies)
        if e.type == TO_GENERATE_COINS:
            Coin.generate(randint(3, 6), collectables)
        if e.type == TO_GENERATE_SHIELD:
            Shield.generate(1, collectables)
        if e.type == TO_LOSE_SHIELD:
            player.protected = False
            pg.mixer.Sound('data/sounds/shield_down.wav').play()

    clock.tick(FPS)
    screen.fill('white')

    col_enemy = pg.sprite.spritecollideany(player, enemies)
    if col_enemy:
        pg.mixer.Sound('data/sounds/enemy_hit.wav').play()
        col_enemy.kill()
        if player.lives < 1:
            running = False
        else:
            player.lives -= 1


    col_coins = pg.sprite.spritecollideany(player, collectables)
    if col_coins:
        col_coins.collect(player)
        print(player.score)


    player_group.draw(screen)
    player_group.update()

    collectables.draw(screen)
    collectables.update()

    enemies.draw(screen)
    enemies.update(player)

    pg.display.update()