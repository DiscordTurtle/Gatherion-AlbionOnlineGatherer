from PIL import ImageGrab, Image
import numpy as np
import cv2
import time
import pyautogui
import random

floater = "floater.png"

def recordScreenBoxFromPoint(x, y, width, height):
    # Screenshots are made from left down corner to right top corner
    left = x - width / 2
    top = y - height / 2
    right = x + width / 2
    bottom = y + height / 2
    screenshoot = ImageGrab.grab(
        bbox=(left, top, right, bottom))
    return np.array(screenshoot)

def imageProcessing(image):
    imageprocessing = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # imageprocessing = cv2.Canny(
    #     imageprocessing, threshold1=200, threshold2=300)
    return imageprocessing

def detectBite():
    average = 0
    sumOfAll = 0
    count = 0
    sum = 0
    lastAverageImg = 0
    averageImg = 0

    floatloc = pyautogui.locateCenterOnScreen(floater)

    while (True):
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        x, y = pyautogui.position()
        # print(x, y)
        # img = recordScreenBoxFromPoint(x, y, 100, 100)
        # img = imageProcessing(img)
        # img = cv2.Canny(
        #     img, threshold1=100, threshold2=320)
        # count = count + 1
        # mean = np.abs(np.mean(img))
        # sumOfAll = sumOfAll + mean
        # average = sumOfAll/count
        # print(average, average - mean)
        # cv2.imshow("test", img)
        # if (average - mean >= 0.5) and count >= 15:
        #     time.sleep(1)
        #     break
        # time.sleep(0.01)

        # TEMPORAL DETECTION
        # print(x, y)
        img = recordScreenBoxFromPoint(x, y, 70, 70)     # get the position of the floaty thing by pyautogui location and then put the mafaka in this
        img = imageProcessing(img)
        img = cv2.Canny(
            img, threshold1=60, threshold2=80)
        averageImg = np.average(img)
        count = count + 1
        sum = sum + averageImg
        average = sum / count
        cv2.imshow("test", img)
        if count >= 15:
            print(np.abs(averageImg/average)/np.abs(lastAverageImg/average))
            if(np.abs(averageImg/average)/np.abs(lastAverageImg/average) >= 1.3):
                time.sleep(0.1 + random.random())
                break
        lastAverageImg = averageImg

    cv2.destroyAllWindows()
    pyautogui.click()

detectBite()
