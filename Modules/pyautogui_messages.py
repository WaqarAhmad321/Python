import pyautogui
import time
time.sleep(5)
count = 0
while count <= 100:
    pyautogui.typewrite("Hello, World!")
    pyautogui.press("Enter")
    count += 1
