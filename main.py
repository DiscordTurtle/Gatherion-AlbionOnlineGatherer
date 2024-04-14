import torch
#stone model
model = torch.hub.load('ultralytics/yolov5','custom', path = 'best1.pt', force_reload=True)

from helper import *
import time
import cv2 as cv
from move import Move
import keyboard

time.sleep(1)




def main():
    
    vision_bool = True
    
    bot_bool = False
    
    window_capture = WindowCapture(Variables.width, Variables.height, Variables.window_rect)
    
    go = Move()
    go.start()

    set_albion_foreground(Variables.albion_hwnd)

    move_albion_to_top_left(Variables.albion_hwnd, Variables.width, Variables.height)
    
    
    while True: 
        screenshot = window_capture.get_screenshot()
        results = model(screenshot)
        
        
        frame = np.squeeze(results.render())
        
        toggle_vision(frame, vision_bool)
        
        #Get rectangles position of detected objects
        rectangles = get_rectangles(results)
        #Get the center position of the rectangles
        centers = get_center(rectangles)
        
        
        if keyboard.is_pressed("c"):
            bot_bool = not bot_bool
            
        #Toggle Vision
        if keyboard.is_pressed("v"):
            vision_bool = not vision_bool            
            
        go.update(centers, bot_bool)
        
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
        
        
        
main()