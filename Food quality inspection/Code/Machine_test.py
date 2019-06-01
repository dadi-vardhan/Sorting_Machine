import numpy as np
import cv2
import serial

img=cv2.imread('biscuit.jpg')
r=150.0/img.shape[1]
dim=(150, int(img.shape[0] * r))
rsimg=cv2.resize(img,dim, interpolation = cv2.INTER_AREA)
# Resize the image
#re = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

blur=cv2.GaussianBlur(rsimg,(21,21),0)
canny = cv2.Canny(blur, 30, 145)
(T, thresh) = cv2.threshold(canny, 0, 255, cv2.THRESH_BINARY)
(cnts, _) = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print ("I count %d contours in this image" % (len(cnts)))
countors = thresh
cv2.drawContours(countors, cnts, -1, (0, 255, 0), 2)
#cv2.imshow("Coins",coins )
cv2.imshow("countors",canny)
cv2.waitKey(0)
defects=len(cnts)
cv2.destroyAllWindows()
if defects > 1:
   ser = serial.Serial("COM1", 19200)
   print(ser)
   ser.write('Y')
else:

   ser = serial.Serial('COM1', 19200)
   print(ser)
   ser.write('N')
   




