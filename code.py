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
global_speed = 1
image_bank_sprites = stage.Bank.from_bmp16("sprite_sheet.bmp")
bullets = []
my_tank = []
tanks = []
irons = []
bricks = []
bushes = []
waters = []
base = []
enemy_lifes = 15


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
        if not DEBUG:
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

    my_tank.append(Tank(3, 7))
    tanks.append(EnemyTank(4, 0, 0, 2))
    tanks.append(EnemyTank(9, 0, 50, 2))
    tanks.append(EnemyTank(0, 0, 100, 2))
    tanks.append(EnemyTank(4, 0, 150, 2))
    tanks.append(EnemyTank(9, 0, 300, 2))
    tanks.append(EnemyTank(0, 0, 400, 2, constants.ENEMY_TANK2))
    tanks.append(EnemyTank(4, 0, 500, 2))
    tanks.append(EnemyTank(9, 0, 600, 2))
    tanks.append(EnemyTank(0, 0, 700, 2))
    tanks.append(EnemyTank(4, 0, 800, 2))
    tanks.append(EnemyTank(9, 0, 900, 2))
    tanks.append(EnemyTank(0, 0, 1000, 2, constants.ENEMY_TANK4))
    tanks.append(EnemyTank(4, 0, 1100, 2))
    tanks.append(EnemyTank(9, 0, 1200, 2))
    tanks.append(EnemyTank(0, 0, 1300, 2, constants.ENEMY_TANK3))

    irons.append(Block(constants.BLOCK_IRON, 0, 6))
    irons.append(Block(constants.BLOCK_IRON, 1, 6))
    irons.append(Block(constants.BLOCK_IRON, 8, 6))
    irons.append(Block(constants.BLOCK_IRON, 9, 6))
    bricks.append(Block(constants.BLOCK_BRICK, 0, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 9, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 1, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 2, 3))
    bricks.append(Block(constants.BLOCK_BRICK, 2, 4))
    bricks.append(Block(constants.BLOCK_BRICK, 7, 3))
    bricks.append(Block(constants.BLOCK_BRICK, 7, 4))
    bricks.append(Block(constants.BLOCK_BRICK, 8, 5))
    bricks.append(Block(constants.BLOCK_BRICK, 1, 5))
    bricks.append(Block(constants.BLOCK_BRICK, 1, 2))
    bricks.append(Block(constants.BLOCK_BRICK, 8, 2))
    bricks.append(Block(constants.BLOCK_BRICK, 3, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 4, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 5, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 6, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 8, 1))
    bricks.append(Block(constants.BLOCK_BRICK, 4, 7))
    bricks.append(Block(constants.BLOCK_BRICK, 4, 6))
    bricks.append(Block(constants.BLOCK_BRICK, 5, 6))
    bricks.append(Block(constants.BLOCK_BRICK, 6, 6))
    bricks.append(Block(constants.BLOCK_BRICK, 6, 7))
    bushes.append(Block(constants.BLOCK_BUSH, 3, 2))
    bushes.append(Block(constants.BLOCK_BUSH, 4, 2))
    bushes.append(Block(constants.BLOCK_BUSH, 5, 2))
    bushes.append(Block(constants.BLOCK_BUSH, 6, 2))
    bushes.append(Block(constants.BLOCK_BUSH, 3, 3))
    bushes.append(Block(constants.BLOCK_BUSH, 3, 4))
    bushes.append(Block(constants.BLOCK_BUSH, 3, 5))
    bushes.append(Block(constants.BLOCK_BUSH, 4, 5))
    bushes.append(Block(constants.BLOCK_BUSH, 5, 5))
    bushes.append(Block(constants.BLOCK_BUSH, 6, 5))
    bushes.append(Block(constants.BLOCK_BUSH, 6, 4))
    bushes.append(Block(constants.BLOCK_BUSH, 6, 3))
    waters.append(Block(constants.BLOCK_WATER, 5, 3))
    waters.append(Block(constants.BLOCK_WATER, 4, 3))
    waters.append(Block(constants.BLOCK_WATER, 5, 4))
    waters.append(Block(constants.BLOCK_WATER, 4, 4))
    base.append(Base(constants.BASE, 5, 7))

    sprites = base + my_tank + tanks + bullets

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = irons + bushes + bricks + sprites + waters
    game.render_block()
    frame = 0

    while True:
        frame += 1
        for sprite in sprites:
            sprite.update(frame)
        game.render_sprites(sprites)
        # game.tick()

def level_two_scene():
    bullets.clear()
    my_tank.clear()
    tanks.clear()
    irons.clear()
    bricks.clear()
    bushes.clear()
    waters.clear()
    base.clear()
    functions.add_sound("game_start.wav")

    tile_offset = 24
    level_tiles = []

    image_level_bank_background1 = stage.Bank.from_bmp16("level_two_background1.bmp")
    image_level_bank_background2 = stage.Bank.from_bmp16("level_two_background2.bmp")

    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background1)
    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles
    game.render_block()

    while True:
        # Wait for 4 seconds
        time.sleep(4.3)
        level_two_game_scene()

def level_two_game_scene():
    pass

def lost():
    bullets.clear()
    my_tank.clear()
    tanks.clear()
    irons.clear()
    bricks.clear()
    bushes.clear()
    waters.clear()
    base.clear()
    functions.add_sound("game_start.wav")

    tile_offset = 20
    level_tiles = []

    image_level_bank_background1 = stage.Bank.from_bmp16("lose_background1.bmp")
    image_level_bank_background2 = stage.Bank.from_bmp16("lose_background2.bmp")

    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background1)
    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles
    game.render_block()

    while True:
        # Wait for 4 seconds
        time.sleep(4.3)
        menu_scene()

class Tank(stage.Sprite):
    def __init__(self, x, y):
        super().__init__(image_bank_sprites, constants.MY_TANK, x * 16, y * 16)
        self.isAlive = True
        self.start_x = x * 16
        self.start_y = y * 16
        self.died_frame = 0
        self.time = 0
        self.my_bullets = []
        self.rotation = 0
        self.speed = 1
        self.lifes = 3
        self.a_button = constants.button_state["button_up"]
        new_bullet = Bullet(2, 1, False)
        self.my_bullets.append(new_bullet)
        bullets.append(new_bullet)

    def update(self, frame):
        super().update()
        if not self.isAlive:
            if not self.died_frame:
                self.died_frame = frame + 50
            elif self.died_frame == frame:
                self.lifes -= 1
                if self.lifes:
                    self.died_frame = 0
                    self.set_frame(constants.MY_TANK, 0)
                    self.move(self.start_x, self.start_y)
                    self.isAlive = True
                else:
                    self.move(-16, -16)
                    self.time = frame + 100
            elif self.time == frame:
                lost()

        else:
            keys = ugame.buttons.get_pressed()

            speed = 0
            if keys & ugame.K_O:
                if self.a_button == constants.button_state["button_up"]:
                    self.a_button = constants.button_state["button_just_pressed"]
                elif self.a_button == constants.button_state["button_just_pressed"]:
                    self.a_button = constants.button_state["button_still_pressed"]
            else:
                if self.a_button == constants.button_state["button_still_pressed"]:
                    self.a_button = constants.button_state["button_released"]
                else:
                    self.a_button = constants.button_state["button_up"]
            if keys & ugame.K_UP != 0:
                self.rotation = 0
                speed = self.speed
            if keys & ugame.K_RIGHT != 0:
                self.rotation = 1
                speed = self.speed
            if keys & ugame.K_DOWN != 0:
                self.rotation = 2
                speed = self.speed
            if keys & ugame.K_LEFT != 0:
                self.rotation = 3
                speed = self.speed
            
            if self.a_button == constants.button_state["button_just_pressed"]:
                for bullet in self.my_bullets:
                    if not bullet.isAlive:
                        bullet.activate(self.x, self.y, self.rotation)
                        break

            no_collision = True
            for block in irons + bricks + waters + base:
                delta_x, delta_y = functions.get_delta(self.rotation, self.speed * global_speed)
                if stage.collide(self.x+delta_x, self.y+delta_y, self.x+15+delta_x, self.y+15+delta_y,
                                block.x, block.y, block.x+15, block.y+15):
                    no_collision = False
                    break

            for tank in tanks:
                if stage.collide(self.x+delta_x, self.y+delta_y,
                                self.x+delta_x+15, self.y+delta_y+15,
                                tank.x, tank.y,
                                tank.x+15, tank.y+15):
                    no_collision = False

            if self.x+delta_x < 0 or self.x+delta_x > 144 or self.y+delta_y < 0 or self.y+delta_y > 112:
                no_collision = False

            if speed:
                self.set_frame(None, self.rotation)
                if no_collision:
                    self.move(self.x + delta_x, self.y + delta_y)

    def kill(self):
        self.set_frame(12)
        self.isAlive = False


class EnemyTank(stage.Sprite):
    def __init__(self, x, y, start_frame, rotation = 0, tank_type = constants.ENEMY_TANK):
        super().__init__(image_bank_sprites, tank_type, -16, -16, 0, rotation)
        self.isActive = False
        self.isAlive = False
        self.rotation = rotation
        self.start_x = x * 16
        self.start_y = y * 16
        self.start_frame = start_frame
        self.next_shoot = 0
        self.next_move = 0

        self.speed = 1
        self.lifes = 0
        self.bullet_speed = 1
        self.strength = 1
        self.tank_type = tank_type

        if self.tank_type == constants.ENEMY_TANK2:
            self.strength = 2
            self.bullet_speed = 4
        elif self.tank_type == constants.ENEMY_TANK3:
            self.speed = 2
            self.bullet_speed = 2
        elif self.tank_type == constants.ENEMY_TANK4:
            self.lifes = 2
            self.bullet_speed = 2

        self.my_bullet = Bullet(self.bullet_speed, self.strength)
        bullets.append(self.my_bullet)

    def update(self, frame):
        super().update()
        # Activate the tank at start frame
        if not self.isActive and frame >= self.start_frame:
            self.isActive = True
            self.isAlive = True
            self.move(self.start_x, self.start_y)

        if self.isAlive:
            global global_speed
            if self.next_shoot < frame:
                self.next_shoot = frame + random.randint(50, 100)
            if self.next_move < frame:
                self.next_move = frame + random.randint(150, 250)

            # Evaluate collision with any objects
            no_collision = True
            delta_x, delta_y = functions.get_delta(self.rotation, self.speed * global_speed)

            for block in irons + bricks + waters + base:
                if block.x != -16:
                    if stage.collide(self.x+delta_x, self.y+delta_y,
                                    self.x+delta_x+15, self.y+delta_y+15,
                                    block.x, block.y,
                                    block.x+15, block.y+15):
                        no_collision = False
                        break

            if no_collision and stage.collide(self.x+delta_x, self.y+delta_y,
                            self.x+delta_x+15, self.y+delta_y+15,
                            my_tank[0].x, my_tank[0].y,
                            my_tank[0].x+15, my_tank[0].y+15):
                no_collision = False

            if no_collision:
                for tank in tanks:
                    if self != tank and tank.isAlive:
                        if stage.collide(self.x+delta_x, self.y+delta_y,
                                        self.x+delta_x+15, self.y+delta_y+15,
                                        tank.x, tank.y,
                                        tank.x+15, tank.y+15):
                            no_collision = False
                            break

            if no_collision:
                self.move(self.x + delta_x, self.y + delta_y)

            if self.next_shoot == frame and not self.my_bullet.isAlive:
                self.my_bullet.activate(self.x, self.y, self.rotation)

            # Evaluate collision with boards
            if self.y > 112 or self.x < 0 or self.x > 144 or self.y < 0:
                self.rotation = (self.rotation + 2) % 4
                self.set_frame(None, self.rotation)
            elif self.next_move == frame:
                self.rotation = random.randint(0, 3)
                self.set_frame(None, self.rotation)

    def kill(self):
        global enemy_lifes
        if self.lifes == 0:
            self.move(-16, -16)
            self.isAlive = False
            enemy_lifes -= 1
        else:
            self.lifes -= 1
        if enemy_lifes == 0:
            time.sleep(3)
            level_two_scene()

class Block(stage.Sprite):
    def __init__(self, type, x, y):
        super().__init__(image_bank_sprites, type, x*16, y*16)
        self.armor = 2 if type == constants.BLOCK_IRON else 1

    def kill(self, strength = 1):
        if self.armor <= strength:
            self.move(-16, -16)

class Base(stage.Sprite):
    def __init__(self, type, x, y):
        super().__init__(image_bank_sprites, type, x*16, y*16)
        self.type = type
        self.isAlive = True
        self.time_t = 0

    def update(self, frame):
        super().update()
        if not self.isAlive:
            time.sleep(3)
            lost()

    def kill(self):
        self.set_frame(15)
        self.isAlive = False

class Bullet(stage.Sprite):
    def __init__(self, speed = 1, strength = 1, isEnemy = True):
        super().__init__(image_bank_sprites, constants.BULLET, -16, -16)
        self.speed = speed
        self.strength = strength
        self.rotation = 1
        self.isAlive = False
        self.isEnemy = isEnemy

    def update(self, frame):
        super().update()

        delta_x, delta_y = functions.get_delta(self.rotation, self.speed)
        if self.isAlive:
            if self.y > 112 or self.x < 0 or self.x > 144 or self.y < 0:
                self.kill()

        if (self.isAlive):
            for block in irons + bricks:
                if stage.collide(self.x+4, self.y+4, self.x+8+delta_x, self.y+8+delta_y,
                            block.x, block.y, block.x+15, block.y+15):
                    self.kill()
                    block.kill(self.strength)
                    break

        if (self.isAlive):
            if stage.collide(self.x+4, self.y+4, self.x+8+delta_x, self.y+8+delta_y,
                        base[0].x, base[0].y, base[0].x+15, base[0].y+15):
                self.kill()
                base[0].kill()

        if self.isAlive:
            if self.isEnemy:
                if stage.collide(self.x+4, self.y+4,
                                    self.x+delta_x+8, self.y+delta_y+8,
                                    my_tank[0].x, my_tank[0].y,
                                    my_tank[0].x+15, my_tank[0].y+15):
                    self.kill()
                    my_tank[0].kill()
            else:
                for tank in tanks:
                    if tank.isAlive:
                        if stage.collide(self.x+4, self.y+4,
                                        self.x+8, self.y+8,
                                        tank.x, tank.y,
                                        tank.x+15, tank.y+15):
                            self.kill()
                            tank.kill()
                            break

        if (self.isAlive):
            for bullet in bullets:
                    if self != bullet:
                        if stage.collide(self.x+delta_x+4, self.y+delta_y+4,
                                        self.x+delta_x+8, self.y+delta_y+8,
                                        bullet.x+4, bullet.y+4,
                                        bullet.x+8, bullet.y+8):
                            self.kill()
                            bullet.kill()
        if (self.isAlive):
            self.move(self.x + delta_x, self.y + delta_y)

    def activate(self, x, y, rotation):
        self.rotation = rotation
        self.x = x
        self.y = y
        self.move(self.x, self.y)
        self.set_frame(None, self.rotation)
        self.isAlive = True

    def kill(self):
        self.isAlive = False
        self.move(-16, -16)

if __name__ == "__main__":
    splash_scene()
