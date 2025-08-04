import keyboard
import pyautogui
import time
from pynput.mouse import Button, Controller
pyautogui.PAUSE = 0.0001
#keyboard.press_and_release('m')
mouse = Controller()

#Gets the position of mouse when m is pressed
pyautogui.FAILSAFE = False
qq = 0
while True:
     keyboard.wait('m')
     x, y = pyautogui.position()
     time.sleep(0.0001)
     pyautogui.moveTo(800, 80)
     time.sleep(0.0001)
     pyautogui.click()
     print(x,y)
