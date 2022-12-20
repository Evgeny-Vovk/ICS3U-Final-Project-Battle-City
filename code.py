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
            level_one_game_scene_test()

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
        level_one_game_scene_test()

image_bank_sprites1 = stage.Bank.from_bmp16("sprite_sheet1.bmp")
image_bank_sprites2 = stage.Bank.from_bmp16("sprite_sheet2.bmp")




class Tank(stage.Sprite):
    def __init__(self, x, y):
        super().__init__(image_bank_sprites1, 8, x * 16, y * 16)
        self.isAlive = True
        self.start_x = x * 16
        self.start_y = y * 16
        self.died_frame = 0
        self.time = 0
        self.my_bullets = []
        self.rotation = 0
        self.speed = 1
        self.bullet_mode = 0
        # self.lifes = 3
        self.lifes = 1
        self.a_button = constants.button_state["button_up"]
        new_bullet = Bullet(2)
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
                    self.set_frame(8, 0)
                    self.move(self.start_x, self.start_y)
                    self.isAlive = True
                else:
                    self.move(-16, -16)
                    self.time = frame + 100
            elif self.time == frame:
                bullets.clear()
                my_tank.clear()
                tanks.clear()
                bricks.clear()
                irons.clear()
                bushes.clear()
                waters.clear()
                global tanks_in_game
                tanks_in_game = 4
                menu_scene()

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

            for bullet in self.my_bullets:
                if bullet.isAlive:
                    for tank in tanks:
                        if stage.collide(bullet.x+4, bullet.y+4,
                                        bullet.x+8, bullet.y+8,
                                        tank.x, tank.y,
                                        tank.x+15, tank.y+15):
                            bullet.kill()
                            tank.kill()
                            break

            no_collision = True
            for brick in bricks:
                delta_x, delta_y = get_delta(self.rotation, self.speed * global_speed)
                if stage.collide(self.x+delta_x, self.y+delta_y, self.x+15+delta_x, self.y+15+delta_y,
                                brick.x, brick.y, brick.x+15, brick.y+15):
                    no_collision = False
                    break

            if self.x+delta_x < 0 or self.x+delta_x > 144 or self.y+delta_y < 0 or self.y+delta_y > 112:
                no_collision = False

            if speed:
                self.set_frame(None, self.rotation)
                if no_collision:
                    self.move(self.x + delta_x, self.y + delta_y)



        # if layer1.tile((self.x + 8) // 16, (self.y + 8) // 16) == 0:
        #     self.kill()
        # else:
        #     sprite.set_frame(9, (frame // 4) * 4)
        #     self.move(self.x + self.dx, self.y)

    def kill(self):
        self.set_frame(12)
        self.isAlive = False


def get_delta(rotation, speed = 1):
    if (rotation == 0):
        dx, dy = 0, -speed
    elif (rotation == 1):
        dx, dy = speed, 0
    elif (rotation == 2):
        dx, dy = 0, speed
    elif (rotation == 3):
        dx, dy = -speed, 0
    return dx, dy


class TankLite(stage.Sprite):
    def __init__(self, x, y, start_frame, speed = 1, rotation = 0):
        super().__init__(image_bank_sprites2, 1, -16, -16, 0, rotation)
        self.isActive = False
        self.isAlive = False
        self.speed = speed
        self.rotation = rotation
        self.start_x = x * 16
        self.start_y = y * 16
        self.start_frame = start_frame
        self.lifes = 3
        self.my_bullets = []
        self.next_shoot = 0
        self.next_move = 0
        for i in range(2):
            new_bullet = Bullet(2)
            self.my_bullets.append(new_bullet)
            bullets.append(new_bullet)

    def update(self, frame):
        super().update()
        # Activate the tank at start frame
        if not self.isActive and frame >= self.start_frame:
            self.isActive = True
            global tanks_in_game, tanks_in_game_max
            tanks_in_game += 1
            tanks_in_game_max += 1
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
            delta_x, delta_y = get_delta(self.rotation, self.speed * global_speed)
            for brick in bricks:
                if stage.collide(self.x+delta_x, self.y+delta_y,
                                 self.x+delta_x+15, self.y+delta_y+15,
                                 brick.x, brick.y,
                                 brick.x+15, brick.y+15):
                    no_collision = False
                    break

            if no_collision:
                self.move(self.x + delta_x, self.y + delta_y)

            if self.next_shoot == frame:
                for bullet in self.my_bullets:
                    if not bullet.isAlive:
                        bullet.activate(self.x, self.y, self.rotation)
                        break

            for bullet in self.my_bullets:
                if stage.collide(bullet.x+4, bullet.y+4,
                                 bullet.x+delta_x+8, bullet.y+delta_y+8,
                                 my_tank[0].x, my_tank[0].y,
                                 my_tank[0].x+15, my_tank[0].y+15):
                    bullet.kill()
                    my_tank[0].kill()
                    break

            # Evaluate collision with boards
            change_rotation = False
            if self.y > 112 or self.x < 0 or self.x > 144 or self.y < 0:
                self.rotation = (self.rotation + 2) % 4
                self.set_frame(None, self.rotation)

            if self.next_move == frame:
                self.rotation = random.randint(0, 3)
                self.set_frame(None, self.rotation)

    def kill(self):
        self.move(-16, -16)
        self.isAlive = False
        global tanks_in_game
        tanks_in_game -= 1



        # if (frame == 380):
        #     my_tank[0].kill()


        # if layer1.tile((self.x + 8) // 16, (self.y + 8) // 16) == 0:
        #     self.kill()
        # else:
        #     sprite.set_frame(9, (frame // 4) * 4)
        #     self.move(self.x + self.dx, self.y)

    # def kill(self):
    #     self.dx = 0
    #     self.move(-16, -16)
class Block(stage.Sprite):
    def __init__(self, type, x, y):
        if (type == "iron"):
            i = 3
        elif (type == "brick"):
            i = 4
        elif (type == "bush"):
            i = 5
        elif (type == "water"):
            i = 6
        super().__init__(image_bank_sprites1, i, x*16, y*16)
        if (type == "wall"):
            self.isAlive = True
        else:
            self.isAlive = False

    def update(self, frame):
        super().update()

    def kill(self):
        self.move(-16, -16)
        self.isAlive = False


class Bullet(stage.Sprite):
    def __init__(self, speed = 1, strength = 1):
        super().__init__(image_bank_sprites1, 11, -16, -16)
        self.speed = speed
        self.strength = strength
        self.rotation = 1
        self.isAlive = False

    def update(self, frame):
        super().update()

        delta_x, delta_y = get_delta(self.rotation, self.speed)
        if self.isAlive:
            if self.y > 112 or self.x < 0 or self.x > 144 or self.y < 0:
                self.kill()
        if (self.isAlive):
            for brick in bricks:
                if stage.collide(self.x+4, self.y+4, self.x+8+delta_x, self.y+8+delta_y,
                            brick.x, brick.y, brick.x+15, brick.y+15):
                    self.kill()
                    brick.kill()
                    break
        if (self.isAlive):
            for iron in irons:
                if stage.collide(self.x+4, self.y+4, self.x+8+delta_x, self.y+8+delta_y,
                            iron.x, iron.y, iron.x+15, iron.y+15):
                    self.kill()
                    if self.strength >= 2:
                        iron.kill()
                    break
        if (self.isAlive):
            self.move(self.x + delta_x, self.y + delta_y)

    def activate(self, x, y, rotation):
        self.rotation = rotation
        self.x = x
        self.y = y
        self.move(self.x, self.y)
        self.set_frame(None, self.rotation)
        self.isAlive = True


        # if layer1.tile((self.x + 8) // 16, (self.y + 8) // 16) == 0:
        #     self.kill()
        # else:
        #     sprite.set_frame(9, (frame // 4) * 4)
        #     self.move(self.x + self.dx, self.y)

    def kill(self):
        self.isAlive = False
        self.move(-16, -16)

bullets = []
my_tank = []
tanks = []
bricks = []
irons = []
bushes = []
waters = []
tanks_in_game = 0
tanks_in_game_max = 0

def level_one_game_scene_test():
    functions.add_sound("game_sound.wav", True)
    tanks_lifes = 25
    global tanks_in_game
    # print(len(bullets))
    # time.sleep(2)

    # a_button = b_button = start_button = select_button = constants.button_state["button_up"]

    my_tank.append(Tank(4, 7))

    # hero = Hero(16, 16)
    # sprites = [bolt, Sparky(104, 96), Sparky(64, 32), Sparky(16, 96),
    #         Sparky(96, 16), hero]

    tanks.append(TankLite(4, 0, 0, 1, 2))
    tanks.append(TankLite(9, 0, 200, 1, 2))
    tanks.append(TankLite(0, 0, 400, 1, 2))
    tanks.append(TankLite(4, 0, 600, 1, 2))
    # tanks.append(TankLite(4, 0, 800, 1, 2))
    # tanks.append(TankLite(9, 0, 1000, 1, 2))
    # tanks.append(TankLite(0, 0, 1200, 1, 2))
    # tanks.append(TankLite(4, 0, 1400, 1, 2))
    # tanks.append(TankLite(9, 0, 1600, 1, 2))

    bricks.append(Block("brick", 3, 1))
    bricks.append(Block("brick", 5, 1))
    bricks.append(Block("brick", 1, 5))
    bricks.append(Block("brick", 2, 5))
    bricks.append(Block("brick", 3, 5))
    bricks.append(Block("brick", 4, 5))
    bricks.append(Block("brick", 5, 5))
    bricks.append(Block("brick", 6, 5))
    bricks.append(Block("brick", 1, 3))
    bricks.append(Block("brick", 3, 3))
    bricks.append(Block("brick", 4, 3))
    bricks.append(Block("brick", 6, 3))
    bushes.append(Block("bush", 3, 5))
    waters.append(Block("water", 2, 5))
    irons.append(Block("iron", 0, 5))

    sprites = my_tank + tanks + bullets + bricks + bushes + waters + irons

    # game.layers = [layer0] + sprites + [layer1]

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites
    game.render_block()
    frame = 0

    # coll = stage.collide(48, 17,
    #                     48 + 15, 17 +15,
    #                     48, 32, 48+15, 32+15)

    # print(coll)
    # time.sleep(2)

    while True:
        # if tanks_in_game < tanks_in_game_max:
        #     if tanks_lifes > 0:
        #         for tank in tanks:
        #             if not tank.isAlive:
        #                 tank.move(20,20)
        #                 tanks_in_game += 1
        #                 tanks_lifes -= 1
        frame += 1
        # print(len(bullets))
        # for b in bullets:
        #     print(b.isAlive)
        # time.sleep(2)
        for sprite in sprites:
            sprite.update(frame)
        game.render_sprites(sprites)
        game.tick()





#================================================

if __name__ == "__main__":
    splash_scene()