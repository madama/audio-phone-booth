
from pad4pi import rpi_gpio
from pygame import mixer
from pathlib import Path
import os, random, time

AUDIO_PATH = "/home/pi/audio/Audio"
AUDIO_NOT_FOUND_PATH = "/home/pi/audio/NOT_FOUND/"
AUDIO_EXTENSION = ".mp3"

KEYPAD = [
    ["F1", "", "F2", "F3", ""],
    ["Down", "7", "Circles", "8", "9"],
    ["Red", "*", "Volume", "0", "#"],
    ["Up", "1", "L", "2", "3"],
    ["Left", "4", "Right", "5", "6"]
]

ROW_PINS = [4, 14, 15, 17, 18]
COL_PINS = [22, 23, 24, 25, 8]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
mixer.init()

print("Init done!")
print("Waiting for keys...")

track = ""

def playAudio(audioFile):
    if mixer.muxis.get_busy:
        mixer.music.stop
    print("Playing {}".format(audioFile))
    if not Path(audioFile).is_file:
        files = os.listdir(AUDIO_NOT_FOUND_PATH)
        notFoundTrack = random.randrange(0, len(files))
        playAudio(notFoundTrack)
    mixer.music.load(audioFile)
    mixer.music.play()


def printKey(key):
    global track
    print(key)
    if key=="#":
        playAudio(AUDIO_PATH+track+AUDIO_EXTENSION)
        track = ""
    elif key=="*":
        print("Reset")
        mixer.music.stop
        track = ""
    else:
        track += key
        print("track: ", track)


keypad.registerKeyPressHandler(printKey)

try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
    print("Quit!")

