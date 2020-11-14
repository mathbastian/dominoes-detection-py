import cv2 as cv2
import numpy as np

def print_results(area, count_of_edges_above, count_of_edges_below):
    if area == AREA_OF_CIRCLE:
        type_of_domino = "círculos"
    else:
        type_of_domino = "quadrados"
    print("Dominó dos",type_of_domino)
    print("Tem", count_of_edges_above, "pontos na parte superior")
    print("Tem", count_of_edges_below, "pontos na parte inferior")
    print("Ao total tem", (count_of_edges_above + count_of_edges_below) ,"pontos")

AREA_OF_SQUARE = 106.0
AREA_OF_CIRCLE = 28.0

# Change image here
img_color = cv2.imread('Domino3.png')

# Get height of image (to know if edges are above or below)
height, width, channels = img_color.shape

# Apply filters
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray, (7, 7), 0)

# Sharpen the image to remove lines
sharpen_kernel = np.array([[-1,-1,-1], [-1,36,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(img_gray, -1, sharpen_kernel)

# Change colors from black to white and vice versa
thresh = cv2.threshold(sharpen,160,255, cv2.THRESH_BINARY_INV)[1]

# Detect edges
countours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
countours = countours[0] if len(countours) == 2 else countours[1]

count_of_edges_above = 0
count_of_edges_below = 0

for countour in countours:
    area = cv2.contourArea(countour)
    x,y,w,h = cv2.boundingRect(countour)
    # Detect if above or below center
    if y < height/2:
        count_of_edges_above = count_of_edges_above + 1
    else:
        count_of_edges_below = count_of_edges_below + 1

print_results(area, count_of_edges_above, count_of_edges_below)