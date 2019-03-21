#import RPi.GPIO as GPIO
#import time
import signal
import sys
from pad4pi import rpi_gpio

#GPIO.setmode(GPIO.BCM)
KEYPAD = [
    ["F1", "", "F2", "F3", ""],
    ["Down", 7, "Circles", 8, 9]
]

ROW_PINS = [4, 14] #15, 17, 18
COL_PINS = [22, 23, 24, 25, 8]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    keypad.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Init done!")

def printKey(key):
    print(key)

keypad.registerKeyPressHandler(printKey)
