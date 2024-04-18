import torch
#stone model
import os
from helper import *
import time
import cv2 as cv
from move import Move
import keyboard
import inquirer
import threading



#THIS WILL for everything except leather and fishing
count_dict = {"tier_2": 0, 
              "tier_3": 0, "tier_3_mob": 0,
              "tier_4":0, "tier_4_mob":0,
              "tier_5":0, "tier_5_mob":0,
              "tier_6":0, "tier_6_mob":0,
              "tier_7":0, "tier_7_mob":0,
              "tier_8":0, "tier_8_mob":0}


#altrenative count dict is for leather only
leather_count_dict = {"tier_2_mob": 0,
                          "tier_3_mob": 0,
                          "tier_4_mob": 0,
                          "tier_5_mob": 0,
                          "tier_6_mob": 0,
                          "tier_7_mob": 0,
                          "tier_8_mob": 0}

#fishing doesnt require one


def count_class_entries(folder, material):
    used_dict = count_dict
    if material == "leather":
        used_dict = leather_count_dict
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(folder + "/" + filename) as f:
                lines = f.readlines()
                for line in lines:
                    try:
                        used_dict[line[0]] += 1
                    except Exception as e:
                        print(e)
    print(count_dict)



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
    
    global folder    
    folder = "input_pictures/input_" + str(material)

    i = 0
    #Show the current count of each class
    count_class_entries(folder)
    
    while True: 
        screenshot = window_capture.get_screenshot()
                
    
        
        #toggle_vision(screenshot, 1)
        print("'s' to save, 'q' to quit")
        
        if keyboard.is_pressed("s"):
            save_image(material, screenshot)
            i = i + 1
            #show the current count of each class every 10 images saved
            if i % 10 == 0 and material != "fish":
                threading.Thread(target=count_class_entries, args=(folder,)).start()
        if keyboard.is_pressed("q"):
            cv.destroyAllWindows()
            break
        

def save_image(material,screenshot):
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