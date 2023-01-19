
import ugame
import stage
import constants
import time

DEBUG = constants.DEBUG

def get_background(loaded_image):
    background = stage.Grid(
        loaded_image,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y,
    )

    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)

    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)

    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)

    background.tile(4, 5, 13)
    background.tile(5, 5, 14)

    return background


def play_sound(loaded_audio, loop = False):
    audio = open(loaded_audio, "rb")
    ugame.audio.mute(constants.mute_audio)
    if DEBUG:
        ugame.audio.mute(True)
    ugame.audio.play(audio, loop = loop)

def stop_sound():
    ugame.audio.stop()

def fill_background(tiles, tile_offset, loaded_image, tile_range = range(0, 16),offset_x = 0 , offset_y = 0):
    for i in tile_range:
        x = (tile_offset+i) % 10
        y = int((tile_offset+i) / 10)
        a_single_tile = stage.Sprite(
            loaded_image,
            i,
            (x * 16 + offset_x),
            (y * 16 + offset_y),
        )
        tiles.append(a_single_tile)
    return tile_offset + 16

def print_text(display, text, x_pos, y_pos):
    t_obj = stage.Text(
        width=len(text), height=10, font=None, buffer=None
    )
    t_obj.move(x_pos, y_pos)
    t_obj.text(text)
    display.append(t_obj)

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