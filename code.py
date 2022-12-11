#!/usr/bin/env python3

# Created by: Evgeny Vovk
# Created on: 2022 Oct
# This file is the splash/first scene for Battle City on PyBadge.

import ugame
import stage
import time
import random
import math

import constants
import functions

DEBUG = constants.DEBUG

def splash_scene():
    # this function is the main game game_scene

    # get sound ready
    functions.add_sound("coin.wav")

    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = functions.get_background(image_bank_background)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        if DEBUG:
            menu_scene()
        else:
            level_one_game_scene()

def menu_scene():
    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    tiles = []
    tile_offset = 0

    image_bank_background1 = stage.Bank.from_bmp16("menu_background1.bmp")
    image_bank_background2 = stage.Bank.from_bmp16("menu_background2.bmp")
    image_bank_background3 = stage.Bank.from_bmp16("menu_background3.bmp")
    image_bank_background4 = stage.Bank.from_bmp16("menu_background4.bmp")
    image_bank_background5 = stage.Bank.from_bmp16("menu_background5.bmp")

    tile_offset = functions.fill_background(tiles, tile_offset, image_bank_background1, range(10, 16))
    tile_offset = functions.fill_background(tiles, tile_offset, image_bank_background2)
    tile_offset = functions.fill_background(tiles, tile_offset, image_bank_background3)
    tile_offset = functions.fill_background(tiles, tile_offset, image_bank_background4)
    tile_offset = functions.fill_background(tiles, tile_offset, image_bank_background5)

    tank = stage.Sprite(
        image_bank_background1,
        1,
        30,
        63,
    )

    display = []
    functions.print_text(display, "High score:", 10, 10)
    functions.print_text(display, "Play", 50, 70)
    functions.print_text(display, "Controls", 50, 85)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [tank] + display + tiles
    game.render_block()

    mode = 0
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            tank.move(30, 63)
            mode = 0
        if keys & ugame.K_DOWN != 0:
            tank.move(30, 78)
            mode = 1
        if keys & ugame.K_START != 0:
            if mode == 0:
                level_one_scene()
            elif mode == 1:
                controls_scene()

        # redraw Sprites
        game.render_sprites([tank])
        game.tick()

def controls_scene():
    pass

def level_one_scene():
    functions.add_sound("game_start.wav")

    tile_offset = 25
    level_tiles = []

    image_level_bank_background1 = stage.Bank.from_bmp16("level_one_background1.bmp")
    image_level_bank_background2 = stage.Bank.from_bmp16("level_one_background2.bmp")

    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background1)
    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles
    game.render_block()

    while True:
        # Wait for 4 seconds
        time.sleep(4.3)
        level_one_game_scene()

def level_one_game_scene():

    functions.add_sound("game_sound.wav", True)

    a_button = b_button = start_button = select_button = constants.button_state["button_up"]

    image_bank_sprites = stage.Bank.from_bmp16("sprite_sheetp1.bmp")
    image_bank_sprites2 = stage.Bank.from_bmp16("sprite_sheetp2.bmp")
    bushes = []
    bush_x = 48
    while bush_x < 160:
        bush = stage.Sprite(
            image_bank_sprites,
            5,
            bush_x,
            16,
        )
        bush_x += 16
        bushes.append(bush)

    brick_walls = []
    brick_wall_x = 80
    while brick_wall_x < 160:
        brick_wall = stage.Sprite(
            image_bank_sprites,
            4,
            brick_wall_x,
            80,
        )
        brick_wall_x += 16
        brick_walls.append(brick_wall)

    tank = stage.Sprite(
            image_bank_sprites,
            8,
            64,
            112,
        )

    enemies = []
    for enemy_number in range(constants.TOTAL_NUMBER_OF_ENEMIES):
        an_enemy = stage.Sprite(
            image_bank_sprites2,
            0,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y,
        )
        enemies.append(an_enemy)

    bullets = []
    for bullet_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_bullet = stage.Sprite(
            image_bank_sprites,
            11,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y,
        )
        bullets.append(a_bullet)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = bushes + brick_walls + [tank] + enemies + bullets
    game.render_block()

    #start = int(time.monotonic())
    #last = -1
    start = int(time.monotonic())
    next = random.randint(0,4)
    next2 = random.randint(1,4)
    tank_direction = 1
    enemy_tank_direction = 1
    while True:
        current = int(time.monotonic()) - start
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_UP != 0:
            tank.move(tank.x, tank.y - 1)
            tank.set_frame(8)
            tank_direction = 1
            if tank.y < 0:
                tank.move(tank.x, tank.y + 1)
        if keys & ugame.K_DOWN != 0:
            tank.move(tank.x, tank.y + 1)
            tank.set_frame(7)
            tank_direction = 2
            if tank.y > 112:
                tank.move(tank.x,tank.y - 1)
        if keys & ugame.K_LEFT != 0:
            tank.move(tank.x - 1, tank.y)
            tank.set_frame(9)
            tank_direction = 3
            if tank.x < 0:
                tank.move(tank.x + 1,tank.y)
        if keys & ugame.K_RIGHT != 0:
            tank.move(tank.x + 1, tank.y)
            tank.set_frame(10)
            tank_direction = 4
            if tank.x > 144:
                tank.move(tank.x - 1,tank.y)
        if keys & ugame.K_START != 0:
            pass

        #if last < int(current / 4):
        #    last = int(current / 4)
        if current >= next:
            random_number = random.randint(1,4)
            next += random_number
            for enemy_number in range(len(enemies)):
                if enemies[enemy_number].x < 0:
                    enemies[enemy_number].move(random.randint(0, 144), 0)
                    break

        # bullet creation
        if a_button == constants.button_state["button_just_pressed"]:
            for bullet_number in range(len(bullets)):
                if bullets[bullet_number].x < 0:
                    bullets[bullet_number].move(tank.x, tank.y)
                    bullet_direction = tank_direction
                    break

        # bullet direction and moving
        for bullet_number in range(len(bullets)):
            if bullets[bullet_number].x != constants.OFF_SCREEN_X:
                if bullet_direction == 1:
                    bullets[bullet_number].move(
                        bullets[bullet_number].x,
                        bullets[bullet_number].y - 2,
                    )
                elif bullet_direction == 2:
                    bullets[bullet_number].move(
                        bullets[bullet_number].x,
                        bullets[bullet_number].y + 2,
                    )
                elif bullet_direction == 3:
                    bullets[bullet_number].move(
                        bullets[bullet_number].x - 2,
                        bullets[bullet_number].y,
                    )
                elif bullet_direction == 4:
                    bullets[bullet_number].move(
                        bullets[bullet_number].x + 2,
                        bullets[bullet_number].y,
                    )
            # move bullet to off screen if it gets past the screen corner
            if bullets[bullet_number].y < -16 or bullets[bullet_number].y > 128 or bullets[bullet_number].x < -16 or bullets[bullet_number].x > 160:
                    bullets[bullet_number].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y,
                    )

            # make the enemy tanks choose random direction
            if current >= next2:
                random_number = random.randint(1,4)
                next2 += random_number
                for enemy_number in range(len(enemies)):
                    enemy_tank_direction = random.randint(1,5)
                    if enemy_tank_direction == 1 or enemy_tank_direction == 2:
                        enemies[enemy_number].set_frame(0)
                        enemies[enemy_number].move(enemies[enemy_number].x, enemies[enemy_number].y + 1)
                    elif enemy_tank_direction == 3:
                        enemies[enemy_number].set_frame(1)
                        enemies[enemy_number].move(enemies[enemy_number].x, enemies[enemy_number].y - 1)
                    elif enemy_tank_direction == 4:
                        enemies[enemy_number].set_frame(2)
                        enemies[enemy_number].move(enemies[enemy_number].x + 1, enemies[enemy_number].y)
                    elif enemy_tank_direction == 5:
                        enemies[enemy_number].set_frame(3)
                        enemies[enemy_number].move(enemies[enemy_number].x - 1, enemies[enemy_number].y)

            # enemy tank goes oof screen
            for enemy_number in range(len(enemies)):
                if enemies[enemy_number].x > 0:
                    if  enemies[enemy_number].x < 0:
                        enemies[enemy_number].move(0, enemies[enemy_number].y)
                    elif  enemies[enemy_number].x > 144:
                        enemies[enemy_number].move(144, enemies[enemy_number].y)
                    elif  enemies[enemy_number].y < 0:
                        enemies[enemy_number].move(enemies[enemy_number].y, 0)
                    elif  enemies[enemy_number].y > 112:
                        enemies[enemy_number].move(enemies[enemy_number].y, 112)

            # collision between tank and a brick wall
            for brick_wall_number in range(len(brick_walls)):
                if brick_walls[brick_wall_number].x > 0:
                    if tank.x > 0:
                        if stage.collide(
                            brick_walls[brick_wall_number].x + 2,
                            brick_walls[brick_wall_number].y + 2,
                            brick_walls[brick_wall_number].x + 15,
                            brick_walls[brick_wall_number].y + 15,
                            tank.x + 2,
                            tank.y + 2,
                            tank.x + 15,
                            tank.y + 15,
                        ): 
                            if keys & ugame.K_DOWN != 0 or keys & ugame.K_UP != 0:
                                if tank.y < brick_walls[brick_wall_number].y:
                                    tank.move(tank.x, tank.y - 1)
                                elif tank.y > brick_walls[brick_wall_number].y:
                                    tank.move(tank.x, tank.y + 1)
                            if keys & ugame.K_RIGHT != 0 or keys & ugame.K_LEFT != 0:
                                if tank.x < brick_walls[brick_wall_number].x:
                                    tank.move(tank.x - 1, tank.y)
                                elif tank.x > brick_walls[brick_wall_number].x:
                                    tank.move(tank.x + 1, tank.y)

            # collision between two enemy tanks
            for enemy_number in range(len(enemies)):
                if enemies[enemy_number].x > 0:
                    for second_enemy_number in range(len(enemies)):
                        if enemies[second_enemy_number].x > 0:
                            if stage.collide(
                                enemies[enemy_number].x + 2,
                                enemies[enemy_number].y + 2,
                                enemies[enemy_number].x + 15,
                                enemies[enemy_number].y + 15,
                                enemies[second_enemy_number].x + 2,
                                enemies[second_enemy_number].y + 2,
                                enemies[second_enemy_number].x + 15,
                                enemies[second_enemy_number].y + 15,
                            ):
                                if enemies[enemy_number].y < enemies[second_enemy_number].y:
                                    enemies[enemy_number].move(enemies[enemy_number].x, enemies[enemy_number].y - 1)
                                elif enemies[enemy_number].y > enemies[second_enemy_number].y:
                                    enemies[enemy_number].move(enemies[enemy_number].x, enemies[enemy_number].y + 1)
                                if enemies[enemy_number].x < enemies[second_enemy_number].x:
                                    enemies[enemy_number].move(enemies[enemy_number].x - 1, enemies[enemy_number].y)
                                elif enemies[enemy_number].x > enemies[second_enemy_number].x:
                                    enemies[enemy_number].move(enemies[enemy_number].x + 1, enemies[enemy_number].y)

        # redraw Sprites
        game.render_sprites([tank] + enemies + bullets)
        game.tick()

if __name__ == "__main__":
    splash_scene()