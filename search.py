import pyautogui
import pygetwindow as gw
import time
from PIL import Image, ImageDraw
import random

cursor = "cursor.png"

def main():
    time.sleep(3)

    title_keyword = "Albion Online Client"
    albion_window = windows = gw.getWindowsWithTitle(title_keyword)
    
    
    if albion_window:
        albion_window = albion_window[0]
        print(f"Found Albion Online client window at position: {albion_window.topleft}")

        # Assuming the window size is 1024x768
        width, height = 1024, 768
        center_x, center_y = calc_center_pos(albion_window.left, albion_window.top, width, height)
        print(f"The center of the window is at position: ({center_x}, {center_y})")

        #screenshot = pyautogui.screenshot()
        #mark_center(screenshot, center_x, center_y)

        # Right click right of the character
        right_click_cords(center_x,center_y)

        time.sleep(1)

        pyautogui.press("n")
        time.sleep(0.25)

        try:
                cursor_loc = pyautogui.locateCenterOnScreen(cursor, confidence=0.85)
                if cursor_loc:
                    print("Cursor location found:", cursor_loc)
                else:
                    print("Cursor not found.")
        except pyautogui.ImageNotFoundException:
                print("Cursor image not found on the screen.")
        except Exception as e:
                print("An error occurred:", str(e))

def calc_center_pos(x,y, width, height):
    center_x = x + width // 2
    center_y = y + height // 2
    return center_x, center_y

def mark_center(image, x, y):
    draw = ImageDraw.Draw(image)
    y=y-70 # up int ocharacter
    x=x+100 # right from the character // if remove this then center
    # Draw a 5x5 red dot
    dot_size = 2
    left_up_point = (x - dot_size, y - dot_size)
    right_down_point = (x + dot_size, y + dot_size)
    draw.ellipse([left_up_point, right_down_point], fill='red')

    # Save the image with the mark
    image.save('screenshot_with_center_mark.png')

def right_click_cords(x,y):
    y=y-70
    x=x+100
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown(button="right")
    time1 = random.uniform(0.05,0.16)
    time.sleep(time1)
    pyautogui.mouseUp(button="right")


main()

