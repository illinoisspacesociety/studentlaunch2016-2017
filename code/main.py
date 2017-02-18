#Main code for image processing. 

# Imports
from SimpleCV import *
from datetime import datetime
import time

# Constants
WIDTH = 0
HEIGHT = 0
RECT_TOLERANCE = 0.5
COLOR_TOLERANCE = 100
DIRECTORY = "/home/pi/images/"
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
	print tol
	blobs = img.findBlobs()
	if not blobs:
		return 0
	rects = blobs.filter([b.isRectangle(tol) for b in blobs])
	return rects
	
# Function to determin if the image has successfully seen the tarps
def check_success():
	##TODO: write function
	return 1
	
# Function to check that blob matches target color
def check_color(blob,target):
	color = blob.meanColor()
	match = (0,0,0)
	for i in range(1,3):
		if(color[i] >= target[i] - COLOR_TOLERANCE and color[i] <= target[i] + COLOR_TOLERANCE):
			match[i] = 1
		i += 1
	if(color[1] and color[2] and color[3]):
		return 1
	return 0
	
# Function to save the image in the given directory
def save_image(img):
	t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
	img.save(DIRECTORY+IMAGE_NAME+t+IMAGE_TYPE)
	return 1

# Function to write given info to log file
def write_log(log):
	f = open('log','a+')
	f.seek(0,2)
	f.write(log+"\n")
	#with open('log','w') as f:
		#f.write(log)
	f.close()
	return 0

if __name__ == '__main__':
	main()
