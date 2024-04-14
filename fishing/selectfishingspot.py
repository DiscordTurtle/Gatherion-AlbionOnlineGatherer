import pyautogui
import keyboard

def fishing_spot_pos():
    # Look at mouse position until P is pressed
    while True:
        if keyboard.is_pressed("p"):
            break
    mousepos = pyautogui.position()
    x = 0
    y = 0

    mousepos = fishing_spot_pos()
    x, y = mousepos
    print("Fishing spot chosen position: ", x, y)
    return mousepos

