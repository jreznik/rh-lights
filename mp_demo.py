import gc
gc.collect()

from machine import Pin
from neopixel import NeoPixel
from time import sleep


flash = Pin(0, Pin.IN)
led = Pin(5, Pin.OUT)
btn = Pin(14, Pin.IN)

Pin(2, Pin.OUT).value(1)
Pin(4, Pin.OUT).value(0)
led.value(0)

# A board of 5x5
board_size = 5 * 5
led_board = NeoPixel(Pin(12, Pin.OUT), board_size)

# Colors
BLACK = OFF = 0, 0, 0
WHITE = 10, 10, 10
RED = 10, 0, 0
ORANGE = 10, 5, 0
YELLOW = 10, 10, 0
GREEN = 0, 10, 0
CYAN = 0, 10, 10
BLUE = 0, 0, 10
VIOLET = PURPLE = PINK = 10, 0, 10
GRAY = 5, 5, 5

COLORS = [WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, VIOLET, GRAY]

# Images
HI = [0, 2, 4, 5, 7, 10, 11, 12, 14, 15, 17, 19, 20, 22, 24]
SMILE = [6, 8, 15, 21, 22, 23, 19]
HEART = [1, 3, 5, 7, 9, 10, 14, 16, 18, 22]


def clear_board():
    for i in range(board_size):
        led_board[i] = OFF
        led_board.write()


def draw_image(items, color):
    for i in items:
        led_board[i] = color
        led_board.write()
        sleep(0.1)
    sleep(5)
    clear_board()


def main():
    # Say hi!
    draw_image(HI, GREEN)
    # Be nice!
    draw_image(SMILE, ORANGE)
    # Show love!
    draw_image(HEART, RED)
    clear_board()


if __name__ == "__main__":
    main()
