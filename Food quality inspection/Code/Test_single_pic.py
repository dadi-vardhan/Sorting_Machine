import numpy as np
import cv2
import serial

# Module-1: Biscuit detection

# Read the source image
img = cv2.imread('biscuit.jpg')

# Resize the image
re = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

# Denoising
dst = cv2.fastNlMeansDenoisingColored(re,None,10,10,7,21)

# Blur the image
blurred = cv2.pyrMeanShiftFiltering(dst,61,91)

# Convet to gray scale
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

# Applying otsu
ret, otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#Apply canny edge detection
edges = cv2.Canny(otsu,10,10)

# Converting gray to bgr
#cimg = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

# Detecting the contours
th, contours,hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(edges, contours,-1,(255,0,0),2)

print ("Number of contours detected %d ->"%len(contours))

# Area of contours
#area = cv2.contourArea(contours)
#print(area)

# Hough circles
#circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,np.array([]), 50, 30,1,100)
#circles = np.uint16(np.around(circles))
#for i in circles[0:]:
    #cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
detect = len(contours)
cv2.imshow('Otsu', otsu)
cv2.imshow('Canny', edges)
#cv2.imshow('Detected circles',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Module-2: Trigger the Pyserial
if detect > 0:  #detect is not specified above specify it in module1 as area of circle = detect(range of area)

    ser = serial.Serial('COM1',9600)
    print(ser)
    ser.write('Y')
else:

    ser = serial.Serial('COM1',9600)
    print(ser)
    ser.write('N')
