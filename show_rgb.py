import pyautogui
while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    print(x, y, px)