#Main code for image processing. 

# Imports
from SimpleCV import *
from datetime import datetime
import time

# Constants
WIDTH = 0
HEIGHT = 0
RECT_TOLERANCE = 0.5
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
		rects = find_rects(img)
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
	
# Function to find rectanges in given image
def find_rects(img, tol=RECT_TOLERANCE):
	blobs = img.findBlobs()
	if not blobs:
		return 0
	rects = blobs.filter([b.isRectangle(tol) for b in blobs])
	return rects
	
def check_success():
	##TODO: write function
	return 1
	
def save_image(img):
	t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
	img.save(DIRECTORY+IMAGE_NAME+t+IMAGE_TYPE)
	return 1

def log(log):
	with open('log','w') as f:
		f.write(log)
	f.closed
	return 0

if __name__ == '__main__':
	main()
