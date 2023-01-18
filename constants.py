#!/user/bin/env python3

# Created by: Evgeny Vovk
# Created on: Oct 2022
# This constants file is for Space Alien game

# PyBadge screen size is 160x128 and sprites are 16x16
DEBUG = 0
mute_audio = False

BLOCK_IRON  = 3
BLOCK_BRICK = 4
BLOCK_BUSH  = 5
BLOCK_WATER = 6
MY_TANK     = 7
ENEMY_TANK1 = 8
ENEMY_TANK2 = 9
ENEMY_TANK3 = 10
ENEMY_TANK4 = 11
EXPLOSION   = 12
BULLET      = 13
BASE        = 14
DEAD_BASE   = 15

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ENEMIES = 5
TOTAL_NUMBER_OF_BULLETS = 1

TANK_SPEED          = 1
ENEMY_TANK_SPEED    = 1
LASER_SPEED         = 2

OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 30
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# palettes
RED_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xf8\x1f\x00\x19\xfc\xe0\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)

BLUE_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)

level1_map = [
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK2],
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK3],
        [4, 0, ENEMY_TANK1],
        [0, 6, BLOCK_IRON],
        [1, 6, BLOCK_IRON],
        [8, 6, BLOCK_IRON],
        [9, 6, BLOCK_IRON],
        [0, 1, BLOCK_BRICK],
        [9, 1, BLOCK_BRICK],
        [1, 1, BLOCK_BRICK],
        [2, 3, BLOCK_BRICK],
        [2, 4, BLOCK_BRICK],
        [7, 3, BLOCK_BRICK],
        [7, 4, BLOCK_BRICK],
        [8, 5, BLOCK_BRICK],
        [1, 5, BLOCK_BRICK],
        [1, 2, BLOCK_BRICK],
        [8, 2, BLOCK_BRICK],
        [3, 1, BLOCK_BRICK],
        [4, 1, BLOCK_BRICK],
        [5, 1, BLOCK_BRICK],
        [6, 1, BLOCK_BRICK],
        [8, 1, BLOCK_BRICK],
        [4, 7, BLOCK_BRICK],
        [4, 6, BLOCK_BRICK],
        [5, 6, BLOCK_BRICK],
        [6, 6, BLOCK_BRICK],
        [6, 7, BLOCK_BRICK],
        [3, 2, BLOCK_BUSH],
        [4, 2, BLOCK_BUSH],
        [5, 2, BLOCK_BUSH],
        [6, 2, BLOCK_BUSH],
        [3, 3, BLOCK_BUSH],
        [3, 4, BLOCK_BUSH],
        [3, 5, BLOCK_BUSH],
        [4, 5, BLOCK_BUSH],
        [5, 5, BLOCK_BUSH],
        [6, 5, BLOCK_BUSH],
        [6, 4, BLOCK_BUSH],
        [6, 3, BLOCK_BUSH],
        [5, 3, BLOCK_WATER],
        [4, 3, BLOCK_WATER],
        [5, 4, BLOCK_WATER],
        [4, 4, BLOCK_WATER],
]

level2_map = [
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK1],
        [4, 0, ENEMY_TANK4],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK2],
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK2],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK1],
        [2, 5, BLOCK_IRON],
        [3, 5, BLOCK_IRON],
        [6, 5, BLOCK_IRON],
        [7, 5, BLOCK_IRON],
        [0, 7, BLOCK_IRON],
        [9, 7, BLOCK_IRON],
        [4, 2, BLOCK_IRON],
        [5, 2, BLOCK_IRON],
        [2, 3, BLOCK_BRICK],
        [7, 3, BLOCK_BRICK],
        [2, 2, BLOCK_BRICK],
        [7, 2, BLOCK_BRICK],
        [0, 4, BLOCK_BRICK],
        [1, 4, BLOCK_BRICK],
        [8, 4, BLOCK_BRICK],
        [9, 4, BLOCK_BRICK],
        [0, 1, BLOCK_BRICK],
        [1, 1, BLOCK_BRICK],
        [8, 1, BLOCK_BRICK],
        [9, 1, BLOCK_BRICK],
        [5, 6, BLOCK_BRICK],
        [4, 7, BLOCK_BRICK],
        [6, 7, BLOCK_BRICK],
        [2, 4, BLOCK_BUSH],
        [3, 4, BLOCK_BUSH],
        [6, 4, BLOCK_BUSH],
        [7, 4, BLOCK_BUSH],
        [0, 2, BLOCK_BUSH],
        [1, 2, BLOCK_BUSH],
        [8, 2, BLOCK_BUSH],
        [9, 2, BLOCK_BUSH],
        [0, 3, BLOCK_BUSH],
        [1, 3, BLOCK_BUSH],
        [8, 3, BLOCK_BUSH],
        [9, 3, BLOCK_BUSH],
        [4, 5, BLOCK_WATER],
        [5, 5, BLOCK_WATER],
]

level3_map = [
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK1],
        [4, 0, ENEMY_TANK4],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK2],
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK1],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK2],
        [0, 7, BLOCK_IRON],
        [9, 7, BLOCK_IRON],
        [4, 6, BLOCK_BRICK],
        [5, 6, BLOCK_BRICK],
        [6, 6, BLOCK_BRICK],
        [2, 1, BLOCK_BRICK],
        [3, 1, BLOCK_BRICK],
        [6, 1, BLOCK_BRICK],
        [7, 1, BLOCK_BRICK],
        [4, 2, BLOCK_BRICK],
        [5, 2, BLOCK_BRICK],
        [0, 5, BLOCK_BRICK],
        [9, 5, BLOCK_BRICK],
        [2, 6, BLOCK_BRICK],
        [3, 6, BLOCK_BRICK],
        [6, 6, BLOCK_BRICK],
        [7, 6, BLOCK_BRICK],
        [3, 2, BLOCK_BUSH],
        [3, 3, BLOCK_BUSH],
        [3, 4, BLOCK_BUSH],
        [3, 5, BLOCK_BUSH],
        [2, 2, BLOCK_BUSH],
        [2, 3, BLOCK_BUSH],
        [2, 4, BLOCK_BUSH],
        [2, 5, BLOCK_BUSH],
        [6, 2, BLOCK_BUSH],
        [6, 3, BLOCK_BUSH],
        [6, 4, BLOCK_BUSH],
        [6, 5, BLOCK_BUSH],
        [7, 2, BLOCK_BUSH],
        [7, 3, BLOCK_BUSH],
        [7, 4, BLOCK_BUSH],
        [7, 5, BLOCK_BUSH],
        [1, 2, BLOCK_WATER],
        [1, 3, BLOCK_WATER],
        [1, 4, BLOCK_WATER],
        [1, 5, BLOCK_WATER],
        [8, 2, BLOCK_WATER],
        [8, 3, BLOCK_WATER],
        [8, 4, BLOCK_WATER],
        [8, 5, BLOCK_WATER],
]

level4_map = [
        [4, 0, ENEMY_TANK3],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK4],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK2],
        [4, 0, ENEMY_TANK1],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK2],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK1],
        [2, 4, BLOCK_IRON],
        [3, 4, BLOCK_IRON],
        [6, 4, BLOCK_IRON],
        [7, 4, BLOCK_IRON],
        [0, 7, BLOCK_IRON],
        [9, 7, BLOCK_IRON],
        [4, 2, BLOCK_IRON],
        [5, 2, BLOCK_IRON],
        [0, 5, BLOCK_BRICK],
        [1, 5, BLOCK_BRICK],
        [2, 5, BLOCK_BRICK],
        [7, 5, BLOCK_BRICK],
        [8, 5, BLOCK_BRICK],
        [9, 5, BLOCK_BRICK],
        [4, 7, BLOCK_BRICK],
        [5, 7, BLOCK_BRICK],
        [2, 1, BLOCK_BRICK],
        [3, 1, BLOCK_BRICK],
        [6, 1, BLOCK_BRICK],
        [7, 1, BLOCK_BRICK],
        [0, 2, BLOCK_BUSH],
        [0, 3, BLOCK_BUSH],
        [0, 4, BLOCK_BUSH],
        [9, 2, BLOCK_BUSH],
        [9, 3, BLOCK_BUSH],
        [9, 4, BLOCK_BUSH],
        [1, 3, BLOCK_WATER],
        [1, 4, BLOCK_WATER],
        [8, 3, BLOCK_WATER],
        [8, 4, BLOCK_WATER],
        [2, 6, BLOCK_WATER],
        [7, 6, BLOCK_WATER],
]

level5_map = [
        [4, 0, ENEMY_TANK3],
        [4, 0, ENEMY_TANK2],
        [9, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK4],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK3],
        [9, 0, ENEMY_TANK2],
        [0, 0, ENEMY_TANK2],
        [4, 0, ENEMY_TANK4],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK4],
        [4, 0, ENEMY_TANK3],
        [9, 0, ENEMY_TANK3],
        [0, 0, ENEMY_TANK2],
        [2, 5, BLOCK_IRON],
        [3, 4, BLOCK_IRON],
        [4, 4, BLOCK_IRON],
        [5, 4, BLOCK_IRON],
        [6, 4, BLOCK_IRON],
        [7, 5, BLOCK_IRON],
        [4, 6, BLOCK_IRON],
        [5, 6, BLOCK_IRON],
        [9, 5, BLOCK_IRON],
        [0, 5, BLOCK_IRON],
        [9, 7, BLOCK_IRON],
        [0, 7, BLOCK_IRON],
        [0, 1, BLOCK_BRICK],
        [1, 2, BLOCK_BRICK],
        [2, 2, BLOCK_BRICK],
        [9, 1, BLOCK_BRICK],
        [8, 2, BLOCK_BRICK],
        [7, 2, BLOCK_BRICK],
        [0, 2, BLOCK_BUSH],
        [0, 3, BLOCK_BUSH],
        [0, 4, BLOCK_BUSH],
        [1, 3, BLOCK_BUSH],
        [9, 2, BLOCK_BUSH],
        [9, 3, BLOCK_BUSH],
        [9, 4, BLOCK_BUSH],
        [8, 3, BLOCK_BUSH],
        [3, 2, BLOCK_BUSH],
        [4, 2, BLOCK_BUSH],
        [5, 2, BLOCK_BUSH],
        [6, 2, BLOCK_BUSH],
        [0, 6, BLOCK_BUSH],
        [1, 6, BLOCK_BUSH],
        [8, 6, BLOCK_BUSH],
        [9, 6, BLOCK_BUSH],
        [1, 7, BLOCK_BUSH],
        [8, 7, BLOCK_BUSH],
        [1, 5, BLOCK_WATER],
        [8, 5, BLOCK_WATER],
        [1, 4, BLOCK_WATER],
        [8, 4, BLOCK_WATER],
        [2, 4, BLOCK_WATER],
        [7, 4, BLOCK_WATER],
]

all_levels_map = [
    level1_map,
    level2_map,
    level3_map,
    level4_map,
    level5_map,
]