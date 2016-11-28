#Script continually takes images from the camera and saves them in a numbered sequence

import SimpleCV

directory = "/home/asa/Documents/StudentLaunch/" #define save directory
img_name = "test_image_" #define image file name
img_type = ".png" #define image file type

cam = SimpleCV.Camera()
i = 0
while True:
	img = cam.getImage()
	img.save(directory+img_name+str(i)+img_type)
	i = i+1
	break #take out to continually take and save images

