from helper import *
import time
import cv2 as cv

time.sleep(1)

vision_bool = True


set_albion_foreground(Variables.albion_hwnd)

move_albion_to_top_left(Variables.albion_hwnd, Variables.width, Variables.height)


while True:
    screenshot = Variables.window_capture.get_screenshot()
    toggle_vision(screenshot, vision_bool)
    
    
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
    
    
    