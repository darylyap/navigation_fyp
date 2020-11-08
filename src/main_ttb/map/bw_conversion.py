#!/usr/bin/env python3

import cv2

file_name = 'straight_square'
full_file_name = file_name + '.png'

image = cv2.imread(full_file_name)

# if image == None: 
#     raise Exception("could not load image !")
    
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, result_image) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#Resize
result_image = cv2.resize(result_image,(300,300),interpolation = cv2.INTER_AREA)
# cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Gray image', gray)
# cv2.imshow('Original image',image)

new_file_name = file_name + '_300x300.pgm'

cv2.imwrite(new_file_name, result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()