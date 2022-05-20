from concurrent.futures import thread
from re import TEMPLATE, template
from unittest import result
import cv2 as cv
from cv2 import imread
from cv2 import minMaxLoc
from cv2 import threshold
import numpy as np

#imagem
image = cv.imread('jpgiscawow.jpg', cv.IMREAD_UNCHANGED)
#template
tempimage = cv.imread('jpgcenario.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(image, tempimage, cv.TM_CCORR_NORMED)


#pegar melhor posição da imagem
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match esquerda superior position: %s' % str(max_loc))
print('Best match percentual: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print ('Found template.')

    #pega dimensões do template
    temp_w = tempimage.shape[1]
    temp_h = tempimage.shape[0]

    esquerdasup = max_loc
    direitainf = (esquerdasup[0] + temp_w, esquerdasup[1] + temp_h)

    cv.rectangle(image, esquerdasup, direitainf,
                    color =(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', image)
    cv.waitKey()

else:
    print('Template not found.')


#cv.imshow('Result', result)
#cv.waitKey()

