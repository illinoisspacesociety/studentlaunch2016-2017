#Script continually takes images from the camera and saves them in a numbered sequence

from SimpleCV import *
import time

directory = "/home/asa/Documents/StudentLaunch/" #define save directory
img_name = "test_image_" #define image file name
img_type = ".png" #define image file type

cam = SimpleCV.Camera()
#cam = Camera(prop_set={'width':1920, 'height':1080}) #replace previous line with this to set resolution
i = 0
while i<4000:
	img = cam.getImage()
	img.save(directory+img_name+str(i)+img_type)
	i = i+1
	#break #comment out to continually take and save images
#testing testing
