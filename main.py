import torch
import warnings
import threading
warnings.filterwarnings("ignore", category=UserWarning)
#stone model
from ultralytics import YOLO 
#model = torch.hub.load('ultralytics/yolov5','custom', path = 'models/limestone_test.pt', force_reload=True)
#model = torch.hub.load('ultralytics/yolov5','custom', path = 'models/yolov8n.pt', force_reload=True)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/best.pt', force_reload=True)
from helper import *
import time
import cv2 as cv
from move import Move
import keyboard
from search import *


time.sleep(1)

pointer_rgb = (74,121,115)
def main():
    
    
    vision_bool = True
    
    bot_bool = False
    
    window_capture = WindowCapture(Variables.width, Variables.height, Variables.window_rect)
    
    go = Move()
    go.start()

    set_albion_foreground(Variables.albion_hwnd)

    move_albion_to_top_left(Variables.albion_hwnd, Variables.width, Variables.height)
    pointer = cv.imread("pointer.jpg")

    
    
    while True: 
        screenshot = window_capture.get_screenshot()
        results = model(screenshot)
        
        
   
        
        frame = np.squeeze(results.render())
        
        


        #cv match template
        res = cv.matchTemplate(screenshot, pointer, cv.TM_CCOEFF_NORMED)
        #draw the circle
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        cv.circle(frame, max_loc, 10, (0, 255, 0), 2)
        print(max_loc)


        threading.Thread(target=find_and_display_pointer, args=(frame,)).start()
        
        # Update circle position if pointer is found
        
            
            
        
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
            
        go.update(centers, bot_bool, vision_bool)
        
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
        
        
        
main()