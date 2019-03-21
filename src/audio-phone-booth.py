#import RPi.GPIO as GPIO
from pad4pi import rpi_gpio
from pygame import mixer
import time

#GPIO.setmode(GPIO.BCM)
KEYPAD = [
    ["F1", "", "F2", "F3", ""],
    ["Down", "7", "Circles", "8", "9"]
]

ROW_PINS = [4, 14] #15, 17, 18
COL_PINS = [22, 23, 24, 25, 8]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
mixer.init()

print("Init done!")

def printKey(key):
    print(key)

keypad.registerKeyPressHandler(printKey)

try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
    print("Quit!")

