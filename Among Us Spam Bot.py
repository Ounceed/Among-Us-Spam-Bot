import pyautogui
from time import sleep

sleep(2)

for i in range(20): # amount of spams
    pyautogui(712,600)
    sleep(0.5)
    pyautogui.typewrite("Yoo the imposter is me :D") # or what ever you want it to be
    pyautogui.press("enter")
    sleep(0.5)
    pyautogui.press("enter")
    sleep(3)