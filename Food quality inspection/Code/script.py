import cv2
import numpy as np

cam_port = 1
fps=30
camera=cv2.VideoCapture(cam_port)
def get_img():
    retval,img=camera.read()
    return img
for i in xrange(fps):
 temp=get_img()
print("Taking image...")
cam_cap=get_img()
file="bisk_img.png"
cv2.imwrite(file, cam_cap)
del(camera)
cv2.waitKey(100)

img=cv2.imread('bisk_img.png')
r=150.0/img.shape[1]
dim=(150, int(img.shape[0] * r))
rsimg=cv2.resize(img,dim, interpolation = cv2.INTER_AREA)
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
   print("Biscuit is broken")
   ser = serial.Serial("/dev/ttyACM0", 19200)
   print(ser)
   ser.write('Y')
else:
   print("biscuit is in good shape")
   ser = serial.Serial('/dev/ttyACM0', 19200)
   print(ser)
   ser.write('N')
   
