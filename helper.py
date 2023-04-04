import win32gui
from window_capture import *
import cv2 as cv

class Variables:
    albion_hwnd = win32gui.FindWindow(None, "Albion Online Client")
    window_rect = win32gui.GetWindowRect(albion_hwnd)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]
    window_capture = WindowCapture(width, height, window_rect)



def set_albion_foreground(albion_hwnd):
    win32gui.SetForegroundWindow(albion_hwnd)
    
def move_albion_to_top_left(albion_hwnd, width, height):
    win32gui.MoveWindow(albion_hwnd, 0, 0, width, height, True)

def toggle_vision(screenshot, bool):
    if bool:
        cv.imshow('Computer Vision', screenshot)

