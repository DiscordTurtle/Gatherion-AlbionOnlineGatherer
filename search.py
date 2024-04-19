
import cv2 as cv
import numpy as np


#pointer_rgb = (97, 179, 255)


pointer_loc = "pointer.jpg"
pointer = cv.imread(pointer_loc)
def find_and_display_pointer(frame):
    #cv match template
    res = cv.matchTemplate(frame, pointer, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    cv.circle(frame, max_loc, 10, (0, 255, 0), 2)
    print(max_loc)