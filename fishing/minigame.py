import pyautogui
import os
import time  # Import the time module

# Get the full path to the image file
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "leftsideminigame.png")
float_image_path = os.path.join(script_dir, "fishingfloat.png")


# Determine position of the minigame bar relative to the position of the albion online window on the monitor 
# OR just find the fishing floaty thing and left click when it gets close to left sidered

def minigame():
    
    # LOCATING THE LEFT BORDER OF THE MINIGAME
    try:
        # Locate the left side of the minigame
        leftloc = pyautogui.locateOnScreen(image_path, confidence=0.8)
        
        # Check if the image was found
        if leftloc is not None:
            print("Minigame left side found at position:", leftloc)
        else:
            print("Minigame left side not found")
    except pyautogui.ImageNotFoundException:
        print("Minigame left side not found")

   
    # CLICKING WHEN IT GETS CLOSE TO THE EDGE
    # Edge + 50 pixels buffer for test
    while True:
        try:
            # Locate the left side of the minigame
            floatloc = pyautogui.locateOnScreen(float_image_path, confidence=0.8)
            
            # Check if the image was found
            if floatloc is not None:
                print("Float found at position:", floatloc)
                # Click the button while float is visible and close to edge
                while floatloc is not None:
                    if floatloc.left <= leftloc.left + 50 : #+50 or less 
                        pyautogui.mouseDown(button="left")
                        time.sleep(1.8)
                        pyautogui.mouseUp(button="left")
            else:
                print("Float not found, breaking loop")
                break
        except pyautogui.ImageNotFoundException:
            print("Float not found")



minigame()
