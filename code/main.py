#Main code for image processing. 

# Imports
from SimpleCV import *
from datetime import datetime
import time

# Constants
WIDTH = 0
HEIGHT = 0
DIRECTORY = "/home/asa/Documents/StudentLaunch/studentlaunch2016-2017/images/"
IMAGE_NAME = "image_"
IMAGE_TYPE = ".png"
LOG_FILE = "log"

# Main function
def main():
	cam = SimpleCV.Camera()
	while(1):
		img = capture_image(cam)
		size = get_size()
		find_blobs(img)
		if(check_success()):
			save_image(img)
			print "Success\n"
		
# Function to capture image from camera
def capture_image(cam):
	img = cam.getImage()
	if(img): return img
	print "Could not get image\n"
	return 0
	
def get_size():
	##TODO: write function
	return 0
	
def find_blobs(img):
	blobs = img.findBlobs()
	if blobs:
		rects = blobs.filter([b.isRectangle(0.1) for b in blobs])
		for rect in rects:
			rect.drawOutline((128,0,0),-1,4)
	return img
	
def check_success():
	##TODO: write function
	return 1
	
def save_image(img):
	t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
	img.save(DIRECTORY+IMAGE_NAME+t+IMAGE_TYPE)
	return 1

def log(log):
	return 0

if __name__ == '__main__':
	main()
