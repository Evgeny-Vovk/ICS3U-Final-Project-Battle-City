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
image_bank_sprites = stage.Bank.from_bmp16("sprite_sheet.bmp")
menu_display = []
controls_display = []
menu_tiles = []
controls_tiles = []
level_tiles = []
menu_tank = []
controls_tank = []
level_number_tile = None

bullets = []
my_tank = None
tanks = []
irons = []
bricks = []
bushes = []
waters = []
base = []
enemy_lifes = 0

class Tank(stage.Sprite):
    def __init__(self, x, y):
        super().__init__(image_bank_sprites, constants.MY_TANK, x * 16, y * 16)
        self.isAlive = True
        self.start_x = x * 16
        self.start_y = y * 16
        self.died_frame = 0
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
        if self.isAlive:
            delta_x, delta_y = functions.get_delta(self.rotation, self.speed * global_speed)
            next_x = self.x+delta_x
            next_y = self.y+delta_y
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
                if stage.collide(next_x, next_y, next_x+15, next_y+15,
                                block.x, block.y, block.x+15, block.y+15):
                    no_collision = False
                    break

            for tank in tanks:
                if stage.collide(next_x, next_y, next_x+15, next_y+15,
                                tank.x, tank.y, tank.x+15, tank.y+15):
                    no_collision = False

            if next_x < 0 or next_x > 144 or next_y < 0 or next_y > 112:
                no_collision = False

            if speed:
                self.set_frame(None, self.rotation)
                if no_collision:
                    self.move(next_x, next_y)

        else:
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

    def kill(self, isBaseDestroyed = False):
        self.set_frame(12)
        self.isAlive = False
        if isBaseDestroyed:
            self.lifes = 1


class EnemyTank(stage.Sprite):
    def __init__(self, x, y, tank_type, start_frame, rotation = 2):
        super().__init__(image_bank_sprites, tank_type, -16, -16, 0, rotation)
        self.isActive = False
        self.isAlive = False
        self.rotation = rotation
        self.start_x = x * 16
        self.start_y = y * 16
        self.start_frame = start_frame
        self.next_shoot = 0
        self.next_change_direction = 0

        self.speed = 1
        self.lifes = 1
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
            self.lifes = 3
            self.bullet_speed = 2

        self.my_bullet = Bullet(self.bullet_speed, self.strength)
        bullets.append(self.my_bullet)

    def update(self, frame):
        super().update()
        global my_tank
        # Activate the tank at start frame
        if not self.isActive and frame >= self.start_frame:
            self.isActive = True
            self.isAlive = True
            self.move(self.start_x, self.start_y)

        if self.isAlive:
            global global_speed
            if self.next_shoot < frame:
                self.next_shoot = frame + random.randint(50, 100)

            if self.next_shoot == frame and not self.my_bullet.isAlive:
                self.my_bullet.activate(self.x, self.y, self.rotation)

            if self.next_change_direction < frame:
                self.next_change_direction = frame + random.randint(150, 250)

            if self.next_change_direction == frame:
                self.rotation = random.randint(0, 3)
                self.set_frame(None, self.rotation)

            # Evaluate collision with any objects
            no_collision = True
            delta_x, delta_y = functions.get_delta(self.rotation, self.speed * global_speed)
            next_x = self.x+delta_x
            next_y = self.y+delta_y

            # a. Evaluate collision with blocks
            for block in irons + bricks + waters + base:
                if block.x != -16:
                    if stage.collide(next_x, next_y, next_x+15, next_y+15,
                                    block.x, block.y, block.x+15, block.y+15):
                        no_collision = False
                        break

            # b. Evaluate collision with my tank
            if no_collision and stage.collide(next_x, next_y, next_x+15, next_y+15,
                            my_tank.x, my_tank.y, my_tank.x+15, my_tank.y+15):
                no_collision = False

            # c. Evaluate collision with enemy tank
            if no_collision:
                for tank in tanks:
                    if self != tank and tank.isAlive:
                        if stage.collide(next_x, next_y, next_x+15, next_y+15,
                                        tank.x, tank.y, tank.x+15, tank.y+15):
                            no_collision = False
                            break

            # d. Evaluate collision with boards
            if no_collision:
                if next_x < 0 or next_x > 144 or next_y < 0 or next_y > 112:
                    self.rotation = (self.rotation + 2) % 4
                    self.set_frame(None, self.rotation)
                    no_collision = False

            if no_collision:
                self.move(next_x, next_y)


    def kill(self):
        global enemy_lifes
        self.lifes -= 1
        if self.lifes == 0:
            self.move(-16, -16)
            self.isAlive = False
            enemy_lifes -= 1
            for tank in tanks:
                if tank == self:
                    tanks.remove(tank)

class Block(stage.Sprite):
    def __init__(self, x, y, block_type):
        super().__init__(image_bank_sprites, block_type, x*16, y*16)
        self.armor = 2 if block_type == constants.BLOCK_IRON else 1

    def kill(self, strength = 1):
        if self.armor <= strength:
            self.move(-16, -16)

class Base(stage.Sprite):
    def __init__(self, x, y, block_type):
        super().__init__(image_bank_sprites, block_type, x*16, y*16)

    def kill(self, strength = 1):
        global my_tank
        self.set_frame(15)
        my_tank.kill(True)

class Bullet(stage.Sprite):
    def __init__(self, speed = 1, strength = 1, isEnemy = True):
        super().__init__(image_bank_sprites, constants.BULLET, -16, -16)
        self.speed = speed
        self.strength = strength
        self.rotation = 1
        self.isAlive = False
        self.isActive = False
        self.isEnemy = isEnemy

    def update(self, frame):
        super().update()
        global my_tank
        delta_x, delta_y = functions.get_delta(self.rotation, self.speed)
        next_x = self.x+delta_x
        next_y = self.y+delta_y

        if self.isAlive:
            if self.y > 112 or self.x < 0 or self.x > 144 or self.y < 0:
                self.kill()

        if (self.isAlive):
            for block in irons + bricks + base:
                if stage.collide(self.x+4, self.y+4, next_x+8, next_y+8,
                            block.x, block.y, block.x+15, block.y+15):
                    self.kill()
                    block.kill(self.strength)
                    break

        if self.isAlive:
            if self.isEnemy:
                if stage.collide(self.x+4, self.y+4, next_x+8, next_y+8,
                                    my_tank.x, my_tank.y, my_tank.x+15, my_tank.y+15):
                    self.kill()
                    my_tank.kill()
            else:
                for tank in tanks:
                    if tank.isAlive:
                        if stage.collide(self.x+4, self.y+4, next_x+8, next_y+8,
                                        tank.x, tank.y, tank.x+15, tank.y+15):
                            self.kill()
                            tank.kill()
                            break

        if (self.isAlive):
            for bullet in bullets:
                    if self != bullet:
                        if stage.collide(self.x+4, self.y+4, next_x+8, next_y+8,
                                        bullet.x+4, bullet.y+4, bullet.x+8, bullet.y+8):
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
        self.isActive = True

    def kill(self):
        self.isAlive = False
        self.move(-16, -16)

def splash_scene():
    # get sound ready
    functions.play_sound("coin.wav")

    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = functions.get_background(image_bank_background)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    del image_bank_background

    time.sleep(2.0)
    functions.stop_sound()

def display_level_name(level_number):
    global level_tiles
    global level_number_tile
    tile_offset = 0

    image_level_bank_background = stage.Bank.from_bmp16("level_background.bmp")
    tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background, range(11, 16), 10, 40)
    if not level_number_tile:
        level_number_tile = stage.Sprite(image_level_bank_background,level_number+2,115,56,)
    level_number_tile.set_frame(level_number+2)

    del image_level_bank_background

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles + [level_number_tile]
    game.render_block()

    time.sleep(4.3)

def load_level_map(level_map, level_number):
    global my_tank
    global enemy_lifes
    if level_number == 0 or level_number == 1:
        base.append(Base(5, 7, constants.BASE))
        my_tank = (Tank(3, 7))
    elif level_number == 2 or level_number == 3:
        base.append(Base(3, 7, constants.BASE))
        base.append(Base(6, 7, constants.BASE))
        if level_number == 2:
            my_tank = (Tank(4, 7))
        elif level_number == 3:
            my_tank = (Tank(3, 6))
    elif level_number == 4:
        base.append(Base(3, 7, constants.BASE))
        base.append(Base(5, 7, constants.BASE))
        base.append(Base(7, 7, constants.BASE))
        my_tank = (Tank(3, 6))
    else:
        exit_game(1)
    for item in level_map:
            if item[2] == constants.BLOCK_IRON:
                irons.append(Block(*item))
            elif item[2] == constants.BLOCK_BRICK:
                bricks.append(Block(*item))
            elif item[2] == constants.BLOCK_BUSH:
                bushes.append(Block(*item))
            elif item[2] == constants.BLOCK_WATER:
                waters.append(Block(*item))
            elif item[2] in [constants.ENEMY_TANK1, constants.ENEMY_TANK2, constants.ENEMY_TANK3, constants.ENEMY_TANK4]:
                tanks.append(EnemyTank(item[0], item[1], item[2], len(tanks)*100))
    enemy_lifes = len(tanks)

def clear_objects():
    global my_tank
    del my_tank
    tanks.clear()
    irons.clear()
    bricks.clear()
    bushes.clear()
    waters.clear()
    base.clear()
    bullets.clear()

def exit_game(success):
    tile_offset = 20
    level_tiles = []

    if success == 1:
        image_level_bank_background1 = stage.Bank.from_bmp16("win_background1.bmp")
        image_level_bank_background2 = stage.Bank.from_bmp16("win_background2.bmp")
        tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background1)
        tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background2)
        functions.play_sound("game_start.wav")
    else:
        image_level_bank_background = stage.Bank.from_bmp16("lose_background.bmp")
        tile_offset = 22
        tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background, range(1,5))
        tile_offset = 32
        tile_offset = functions.fill_background(level_tiles, tile_offset, image_level_bank_background, range(11, 15))

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles
    game.render_block()

    time.sleep(4.3)

def game_scene(level_number, level_map):
    global enemy_lifes
    global my_tank

    functions.play_sound("game_start.wav")
    display_level_name(level_number)
    functions.stop_sound()

    functions.play_sound("game_sound.wav", True)
    load_level_map(level_map, level_number)

    sprites = [my_tank] + tanks + bullets

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = irons + bushes + bricks + sprites + waters + base
    game.render_block()
    frame = 0

    while enemy_lifes > 0 and my_tank.lifes > 0:
        frame += 1
        for sprite in sprites:
            sprite.update(frame)
        game.render_sprites(sprites)

    isLevelSucceed = True if my_tank.isAlive else False
    number = 0
    clear_objects()
    functions.stop_sound()

    return isLevelSucceed

def get_selected_menu():
    if not len(menu_tiles):
        tile_offset = 0

        image_bank_background1 = stage.Bank.from_bmp16("menu_background1.bmp")
        image_bank_background2 = stage.Bank.from_bmp16("menu_background2.bmp")
        image_bank_background3 = stage.Bank.from_bmp16("menu_background3.bmp")
        image_bank_background4 = stage.Bank.from_bmp16("menu_background4.bmp")
        image_bank_background5 = stage.Bank.from_bmp16("menu_background5.bmp")

        tile_offset = functions.fill_background(menu_tiles, tile_offset, image_bank_background1, range(10, 16))
        tile_offset = functions.fill_background(menu_tiles, tile_offset, image_bank_background2)
        tile_offset = functions.fill_background(menu_tiles, tile_offset, image_bank_background3)
        tile_offset = functions.fill_background(menu_tiles, tile_offset, image_bank_background4)
        tile_offset = functions.fill_background(menu_tiles, tile_offset, image_bank_background5)

        del image_bank_background1
        del image_bank_background2
        del image_bank_background3
        del image_bank_background4
        del image_bank_background5

    if not len(menu_display):
        functions.print_text(menu_display, "Play", 50, 70)
        functions.print_text(menu_display, "Controls", 50, 85)


    if not len(menu_tank):
        image_bank_background = stage.Bank.from_bmp16("menu_background1.bmp")
        tank = stage.Sprite(
            image_bank_background,
            1,
            30,
            63,
        )
        menu_tank.append(tank)
        del image_bank_background

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = menu_tank + menu_display + menu_tiles
    game.render_block()

    menu_tank[0].move(30, 63)
    mode = 0
    keys = 0
    while True:
    # get user input
        pressed_keys = ugame.buttons.get_pressed()
        if keys != pressed_keys:
            while pressed_keys == ugame.buttons.get_pressed():
                time.sleep(0.1)
            keys = pressed_keys

            if keys & ugame.K_UP != 0:
                menu_tank[0].move(30, 63)
                mode = 0
            if keys & ugame.K_DOWN != 0:
                menu_tank[0].move(30, 78)
                mode = 1
            if keys & ugame.K_START != 0:
                break
            if keys & ugame.K_SELECT != 0:
                constants.mute_audio = not constants.mute_audio
            # redraw Sprites
            game.render_sprites(menu_tank)
            game.tick()
        else:
            time.sleep(0.1)

    return mode

def controls_scene():
    if not len(controls_tiles):
        tile_offset = 16

        image_bank_background1 = stage.Bank.from_bmp16("controls_background1.bmp")
        image_bank_background2 = stage.Bank.from_bmp16("controls_background2.bmp")
        image_bank_background3 = stage.Bank.from_bmp16("controls_background3.bmp")

        tile_offset = functions.fill_background(controls_tiles, tile_offset, image_bank_background1)
        tile_offset = functions.fill_background(controls_tiles, tile_offset, image_bank_background2)
        tile_offset = functions.fill_background(controls_tiles, tile_offset, image_bank_background3)

        del image_bank_background1
        del image_bank_background2
        del image_bank_background3

    if not len(controls_display):
        functions.print_text(controls_display, "Mute - Select", 5, 90)
        functions.print_text(controls_display, "Confirm - Start", 5, 100)
        functions.print_text(controls_display, "Shoot - A", 5, 110)
        functions.print_text(controls_display, "Move - Up,Down,Left", 5, 20)
        functions.print_text(controls_display, "And Right", 5, 30)
        functions.print_text(controls_display, "Exit", 30, 5)


    if not len(controls_tank):
        image_bank_background = stage.Bank.from_bmp16("menu_background1.bmp")
        tank = stage.Sprite(
            image_bank_background,
            1,
            10,
            -3,
        )
        controls_tank.append(tank)
        del image_bank_background

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = controls_tank + controls_display + controls_tiles
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            return
        # redraw Sprites
        game.render_sprites(controls_tank)
        game.tick()

    return mode

def main_scene():
    #AV: ugame.audio.mute(True)
    #AV: ugame.audio.stop()
    # this function is the main game game_scene

    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    splash_scene()

    if DEBUG:
        status = game_scene(constants.all_levels_map)
        print(status)
        time.sleep(10.0)

    mode = 0
    while True:
        mode = get_selected_menu()
        if mode == 0:
            status = True
            for level_number, level_map in enumerate(constants.all_levels_map):
                if status:
                    status = game_scene(level_number, level_map)
                else:
                    exit_game(0)
                    break
        elif mode == 1:
            controls_scene()

if __name__ == "__main__":
    main_scene()
