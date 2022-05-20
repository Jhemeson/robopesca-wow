import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision


# initialize the WindowCapture class
wincap = WindowCapture('World of Warcraft')

# load the trained model
cascade_bobber = cv.CascadeClassifier('cascade/cascade.xml')
# load an empty Vision class
vision_bobber = Vision(None)


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # do object detection
    rectangles = cascade_bobber.detectMultiScale(screenshot)

    # draw the detection results onto the original image
    detection_image = vision_bobber.draw_rectangles(screenshot, rectangles)

    # display the images
    cv.imshow('Matches', detection_image)


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')