from selectfishingspot import fishing_spot_pos
from minigame import minigame
import pyautogui, time, keyboard

# Select fishing spot
mousepos = fishing_spot_pos
while True:
    if keyboard.is_pressed("p"):
            break
    
    # Cast rod
    pyautogui.moveTo(mousepos)
    pyautogui.mouseDown(button="left")
    time.sleep(1.5)
    pyautogui.mouseUp(button="left")

    # Wait till fish pulls
    # how find this shit?

    # When fish pulls click
    pyautogui.click()

    # Do minigame
    minigame()
    
   

