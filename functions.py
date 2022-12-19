import ugame
import stage
import constants

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


def add_sound(loaded_audio, loop = False):
    audio = open(loaded_audio, "rb")
    sound = ugame.audio
    sound.stop()
    if DEBUG:
        sound.mute(True)
    sound.play(audio, loop = loop)

def fill_background(tiles, tile_offset, loaded_image, tile_range = range(0, 16)):
    for i in tile_range:
        x = (tile_offset+i) % 10
        y = int((tile_offset+i) / 10)
        a_single_tile = stage.Sprite(
            loaded_image,
            i,
            (x * 16),
            (y * 16),
        )
        tiles.append(a_single_tile)
    return tile_offset + 16

def print_text(display, text, x_pos, y_pos):
    t_obj = stage.Text(
        width=len(text), height=1, font=None, buffer=None
    )
    t_obj.move(x_pos, y_pos)
    t_obj.text(text)
    display.append(t_obj)