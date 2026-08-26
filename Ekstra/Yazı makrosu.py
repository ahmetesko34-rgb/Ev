import pyautogui
import time
import keyboard

time.sleep(5)

while True:
    if keyboard.is_pressed("q"):
        print("Durduruldu")
        break

    pyautogui.write('BB')
    pyautogui.press("Enter")

    time.sleep(0.1)


