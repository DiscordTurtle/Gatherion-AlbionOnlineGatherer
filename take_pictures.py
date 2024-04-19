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
    
    # Initialize counts for each tier
    tier_keys = ["tier_2", "tier_3", "tier_3_mob", "tier_4", "tier_4_mob", "tier_5", 
                 "tier_5_mob", "tier_6", "tier_6_mob", "tier_7", "tier_7_mob", 
                 "tier_8", "tier_8_mob"]
    tier_counts = {key: 0 for key in tier_keys}
    
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename)) as f:
                lines = f.readlines()
                for line in lines:
                    first_character = line.strip()[0]  # Get the first character of the line
                    if first_character.isdigit():  # Check if the first character is a digit
                        first_integer = int(first_character)  # Convert the first character to an integer
                        if first_integer >= 0 and first_integer <= len(tier_keys)-1:  # Check if the integer is within the range of tier keys
                            tier_key = tier_keys[first_integer]  # Get the corresponding tier key
                            if tier_key in tier_counts:
                                tier_counts[tier_key] += 1
    
    # Print counts for each tier
    print("Material Class Counts:")
    for tier, count in tier_counts.items():
        print(f"{tier.capitalize()}: {count}")

    # Optionally, you can update the global count_dict if needed
    # count_dict.update(tier_counts)







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
    count_class_entries(folder, material)
    
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
    
#main()

main()