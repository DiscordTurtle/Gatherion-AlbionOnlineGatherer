from window_capture import *
import cv2 as cv
import time
class Variables:
    albion_hwnd = win32gui.FindWindow(None, "Albion Online Client")
    window_rect = win32gui.GetWindowRect(albion_hwnd)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]
    window_capture = WindowCapture(width, height, window_rect)

time.sleep(1)
win32gui.SetForegroundWindow(Variables.albion_hwnd)
win32gui.MoveWindow(Variables.albion_hwnd, 0, 0, Variables.width, Variables.height, True)


while True:
    screenshot = Variables.window_capture.get_screenshot()
    cv.imshow('Computer Vision', screenshot)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()