import keyboard
import pyautogui
import time
from pynput.mouse import Button, Controller

mouse = Controller()

#Instant RC tank in gta 5
pyautogui.FAILSAFE = False
qq = 0
while True:
     keyboard.wait('0')
     keyboard.press_and_release('m')
     time.sleep(0.07)
     mouse.scroll(0, -2)
     time.sleep(0.07)
     mouse.scroll(0, -2)
#         keyboard.press_and_release('down')
#         time.sleep(1)
#         keyboard.press_and_release('down')
     time.sleep(0.07)
     keyboard.press_and_release('enter')
     time.sleep(0.07)
     mouse.scroll(0, 4)
     time.sleep(0.07)
     mouse.scroll(0, 4)
     time.sleep(0.07)
     mouse.scroll(0, 4)
     time.sleep(0.07)
     mouse.scroll(0, 4)
#         keyboard.press_and_release('up')
#         time.sleep(1)
#         keyboard.press_and_release('up')
#         time.sleep(1)
#         keyboard.press_and_release('up')
#         time.sleep(1)
#         keyboard.press_and_release('up')
     time.sleep(0.07)
     keyboard.press_and_release('enter')
     time.sleep(0.07)
     qq += 1
