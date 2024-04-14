import torch
#stone model

from helper import *
import time
import cv2 as cv
from move import Move
import keyboard

def main():
    
    window_capture = WindowCapture(Variables.width, Variables.height, Variables.window_rect)
    
    set_albion_foreground(Variables.albion_hwnd)

    move_albion_to_top_left(Variables.albion_hwnd, Variables.width, Variables.height)
    
    
    while True: 
        screenshot = window_capture.get_screenshot()
                
        
        toggle_vision(screenshot, 1)
        
              
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
        
        
        
main()