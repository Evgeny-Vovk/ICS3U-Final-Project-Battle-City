#!/user/bin/env python3

# Created by: Evgeny Vovk
# Created on: Oct 2022
# This constants file is for Space Alien game

# PyBadge screen size is 160x128 and sprites are 16x16
DEBUG = 1


BLOCK_IRON  = 3
BLOCK_BRICK = 4
BLOCK_BUSH  = 5
BLOCK_WATER = 6
MY_TANK     = 7
ENEMY_TANK  = 8
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
