import numpy as np
import cv2

red = input("red")
green = input("green")
blue = input("blue")

color = np.uint8([[[red, green, blue]]])  #Blue Green Red
hsvcolor = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

reg = (hsvcolor[0][0][0], hsvcolor[0][0][1], hsvcolor[0][0][2])
lower = hsvcolor[0][0][0]-10, hsvcolor[0][0][1]-100, hsvcolor[0][0][2]-100
upper = (hsvcolor[0][0][0]+10, hsvcolor[0][0][1]+100, hsvcolor[0][0][2]+100)

regarray = []
lowerarray = []
upperarray = []

for item in reg:
    regarray.append(item)

for item in lower:
    lowerarray.append(item)

for item in upper:
    upperarray.append(item)

if lowerarray[0] <= 0:  #lower test for braking
    lowerarray[0] = 0
if lowerarray[1] <= 0:
    lowerarray[1] = 0
if lowerarray[2] <= 0:
    lowerarray[2] = 0

if upperarray[0] >= 180:  #upper test for braking
    upperarray[0] = 180
if upperarray[1] >= 255:
    upperarray[1] = 255
if upperarray[2] >= 255:
    upperarray[2] = 255

print("regular HSV color:"+str(regarray))
print("lower HSV color:"+str(lowerarray))
print("upper HSV color:"+str(upperarray))

print("regular HSV color:"+str(reg))
print("lower HSV color:"+str(lower))
print("upper HSV color:"+str(upper))
