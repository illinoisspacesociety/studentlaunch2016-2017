#Main code for image processing. 

# Imports
from SimpleCV import *
from datetime import datetime
import time

# Constants
WIDTH = 1280
HEIGHT = 720
RECT_TOLERANCE = 0.2
COLOR_TOLERANCE = 1
#SIZE_TOLERANCE = some number
#DIRECTORY = "/home/pi/images/"
DIRECTORY = "/home/asa/Documents/StudentLaunch/images/"
IMAGE_NAME = "image_"
IMAGE_TYPE = ".png"
LOG_FILE = "/home/pi/studentlaunch2016-2017/code/log"
DL = True
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)

# Main function
def main():
	cam = SimpleCV.Camera(prop_set={'width':WIDTH, 'height':HEIGHT})
	i = 0
	while(i<20000): 
		img = capture_image(cam)
		size = get_size()
		#rects = find_rects(img)
		tarps = find_tarps(img)
		draw_blobs(img, tarps)
		i += 1
		#if(check_success()):
		if(tarps):
			save_image(img,with_dl=False)
			write_log(t)
		
# Function to capture image from camera
def capture_image(cam):
	img = cam.getImage()
	if(img): return img
	print "Could not get image\n"
	return False

# Function to draw blob outlines on given image's drawing layer
def draw_blobs(img, blobs):
	for blob in blobs:
		blob.drawOutline((128,0,0),width=4,layer=img.dl())

# Function to get the size of the tarps in pixels based on altimeter data
def get_size():
	##TODO: write function
    #Read current altitude from altimeter data
    #Navigate through relevant altitude-to-tarp size table
	return False

def find_tarps(img):
	tarps = color_check(img,RED) + color_check(img,BLUE) + color_check(img,YELLOW)
    tarps.filter(filter_size(tarps)) #define filter_size
	return tarps

def filter_size(blobs, tol = SIZE_TOLERANCE):
    tarp_size = get_size()
    return tarp_size >= blobs.area() - tol and tarp_size <= blobs.area() + tol
	
# Function that returns blobs of a certain RGB color from an image
def color_check(img, color):
	c = img.colorDistance(color)
	b = c.binarize(140)
	blobs = img.findBlobsFromMask(b)
	if blobs:
		return blobs

# Function to find rectanges in given image
# Eventually this and find_correct_size can be combined into a single function
def find_rects(img, tol=RECT_TOLERANCE):
	#print tol
	blobs = img.findBlobs()
	if not blobs:
		return False
	rects = blobs.filter([b.isRectangle(tol) for b in blobs])
	return rects

# Function to filter out the blobs that are not the correct size
# Should be called AFTER find_rects
#def find_correct_size(img, tol = SIZE_TOLERANCE):
#    blobs = img.findBlobs()
#    if not blobs:
#        return False
#    tarp_size = get_size()
#    correct_size_blobs = blobs.filter(tarp_size >= blobs.area() - tol and tarp_size <= blobs.area() + tol)
#    return correct_size_blobs
	
# Function to determine if the image has successfully seen the tarps
def check_success():
	##TODO: write function
	return True
	
# Function to check that blob matches target color
# Uses Hue comparison
def check_color(blob,target):
	color = blob.meanColor()
	hue = rgb_to_hue(color)
	target_hue = rgb_to_hue(target)
	if (hue >= target_hue - COLOR_TOLERANCE and hue <= target_hue + COLOR_TOLERANCE):
		return True
	return False
	
# Function to check that blobs matches target color
# Uses RGB value comparison
def check_color2(blob,target):
	color = blob.meanColor()
	test = [0,0,0]
	tol = COLOR_TOLERANCE
	for i in range(0,3):
		c = color[i]
		t = target[i]
		test[i] = (c >= t - tol and c <= t + tol)
	return (test[0] and test[1] and test[2])
	
# Function to get the hue of an RGB value
def rgb_to_hue(color):
	R = float(color[0])
	G = float(color[1])
	B = float(color[2])
	alpha = 1/2 * (2*R-G-B)
	beta = sqrt(3)/2 * (G-B)
	H = atan2(beta,alpha)
	return H
	
# Function to save the image in the given directory
# Set with_dl=True to save two copies: one w/Drawing layer and one w/o
def save_image(img,with_dl=False):
	t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
	img.save(DIRECTORY+IMAGE_NAME+t+IMAGE_TYPE)
	if(with_dl):
		img.dl().clear()
		img.save(DIRECTORY+IMAGE_NAME+t+"_nodl"+IMAGE_TYPE)
	return 1
	
def save_test_image(img,text):
	img.save(DIRECTORY+text+IMAGE_TYPE)

# Function to write given info to log file
def write_log(log):
	f = open(LOG_FILE,'a+')
	f.seek(0,2)
	f.write(log+"\n")
	f.close()
	return 0

if __name__ == '__main__':
	main()
