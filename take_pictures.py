import torch
#stone model
import os
from helper import *
import time
import cv2 as cv
from move import Move
import keyboard
import inquirer



def main():
    
    window_capture = WindowCapture(Variables.width, Variables.height, Variables.window_rect)
    
    set_albion_foreground(Variables.albion_hwnd)

    move_albion_to_top_left(Variables.albion_hwnd, Variables.width, Variables.height)
    
    
    material = ""
    while not material:
        material = input("Enter material name (fiber, fish, leather, ore, stone, wood) : ")
        if material not in ["fiber", "fish", "leather", "ore", "stone", "wood"]:
            print("Invalid material")
            material = ""
    while True: 
        screenshot = window_capture.get_screenshot()
                
        
        #toggle_vision(screenshot, 1)
        print("'s' to save, 'q' to quit")
        
        if keyboard.is_pressed("s"):
            
            
            save_image(material, screenshot)
    
              
        if keyboard.is_pressed("q"):
            cv.destroyAllWindows()
            break
        

def save_image(material,screenshot):
    folder = "input_pictures/input_" + str(material)
    max = get_max_from_folder(folder)
    cv.imwrite(folder + f"/{material}_{max}.jpg", screenshot)
    max += 1
    print(f"Saved {material}_{max}.jpg")
    time.sleep(0.2)

        
        
def get_max_from_folder(folder):
    max = 0
    for filename in os.listdir(folder):
            #filename example stone_1.jpg
            num = int(filename.split("_")[1].split(".")[0])
            if num > max:
                max = num
    print(f"Max: {max}")
    return max + 1
    
main()