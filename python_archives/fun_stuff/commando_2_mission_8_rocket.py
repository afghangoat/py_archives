import keyboard
from pyautogui import *
import random
import time
from pynput.mouse import Button, Controller
PAUSE = 0.00001

#A program which helps you dodge the boss 4 attacks of the flash game commando 2
mouse = Controller()
FAILSAFE = False
qq = 0
while True:
     keyboard.wait('r')
     sleep(0.57)
     keyDown("w")
     sleep(0.01)
     keyUp("w")
     keyDown("d")  # pressing down key 'a'
     sleep(1.5)  # how ever long you want
     keyUp("d")