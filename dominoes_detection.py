import cv2 as cv2
import numpy as np

MAX_HEIGHT = 253
MAX_LENGTH = 142

count_of_circles_above = 0
count_of_circles_below = 0

count_of_squares_above = 0
count_of_squares_below = 0

img_color = cv2.imread('Domino1.png')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray, (7, 7), 0)

# Detect circles - refine it to not detect squares...
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 2, minDist=15, param2=60)

# Detect squares - check last link of sources.txt


if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x,y,r) in circles:
        if y < MAX_HEIGHT/2:
            count_of_circles_above = count_of_circles_above + 1
        else:
            count_of_circles_below = count_of_circles_below + 1

# Print results
print("Círculos acima: ",count_of_circles_above)
print("Círculos abaixo: ",count_of_circles_below)