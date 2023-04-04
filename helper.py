import win32gui
from window_capture import *
import cv2 as cv

class Variables:
    albion_hwnd = win32gui.FindWindow(None, "Albion Online Client")
    window_rect = win32gui.GetWindowRect(albion_hwnd)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]
    



def set_albion_foreground(albion_hwnd):
    win32gui.SetForegroundWindow(albion_hwnd)
    
def move_albion_to_top_left(albion_hwnd, width, height):
    win32gui.MoveWindow(albion_hwnd, 0, 0, width, height, True)

def toggle_vision(frame, bool):
    if bool:
        cv.imshow('Computer Vision', frame)

def get_center(rectangles):
    centers = []
    for i in rectangles:
        x = int(i[0]+((i[2]-i[0])/2))
        y = int(i[1]+((i[3]-i[1])/2))
        centers.append([x, y])
        #print(centers)
    return centers


def get_rectangles(results):
    rectangles = []
    x = results.xyxy[0].tolist()
    for i in x:
        rectangles.append(i[:-2])
    return rectangles
