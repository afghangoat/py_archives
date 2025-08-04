import keyboard
import pyautogui
import random
import time
from pynput.mouse import Button, Controller
pyautogui.PAUSE = 0.00001

mouse = Controller()

#PVZ I Zombie endless jockey macro
pyautogui.FAILSAFE = False
qq = 0
while True:
     keyboard.wait('0')
     for i in range(6):
           x, y = pyautogui.position()
          #     pyautogui.moveTo(800, 80)
          #     pyautogui.click()
          pyautogui.moveTo(x, y)
          pyautogui.click()
     time.sleep(10)