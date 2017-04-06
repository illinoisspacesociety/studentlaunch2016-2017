# Main code for image processing. 
# Authors: Asa Bromenschenkel (ADraicBrom)
# Started: Fall 2016

# Imports
from SimpleCV import *
from datetime import datetime
import time
import RPi.GPIO as GPIO
import math # need this for square root and power in custom color_check_helper function

# Constants
WIDTH = 1280
HEIGHT = 720
RECT_TOLERANCE = 0.3
BIN_TOLERANCE = 130
SIZE_TOLERANCE = 0.10
SIZE_MAX = 40000
SIZE_MIN = 100
COLOR_TOLERANCE = 1 #I think this will have to be higher
DIRECTORY = "/home/pi/images/"
#DIRECTORY = "/home/asa/Documents/StudentLaunch/images/"
IMAGE_NAME = "tarps_"
IMAGE_TYPE = ".png"
LOG_FILE = "/home/pi/studentlaunch2016-2017/code/log"
DL = True
#BLUE = (0,32,91)
#RED = (166,9,61)
#YELLOW = (255,209,0)
BLUE = (0,0,255)    # These should be updated with the actual RGB values
RED = (255,0,0)
YELLOW = (255,255,0)
BUZZER_PIN = 4

# Main function
def main():
	t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
	write_log("\n"+t+", Starting Code\n")
	while(1):
		t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
		try:
			cam = SimpleCV.Camera(prop_set={'width':WIDTH, 'height':HEIGHT})
			img = capture_image(cam)
			write_log(t+", Camera initiated")
			break
		except:
			write_log(t+", Could not access camera")
			time.sleep(0.5)
			pass
	i = 0
	buzzer = buzzer_init()
	write_log(t+", Buzzer initiated")
	while(i<20000): 
		img = capture_image(cam)
		size = get_size()
		tarps = find_tarps(img)
		i += 1
		t = datetime.now().strftime("%Y%m%d_%H%M%S%f")
		if(tarps[0]!=0 or tarps[1]!=0 or tarps[2]!=0):
			for idx, blobs in enumerate(tarps):
				if(blobs!=0):
					size = filter_size(blobs)
					rects = filter_rects(size)
					color = (0,0,0)
					if(idx==0): color = RED
					elif(idx==1): color = BLUE
					elif(idx==2): color = YELLOW
					draw_blobs(img,rects,color)
			save_image(img,t)
		else:
			write_log(t+", No tarps found")
	buzzer.stop()
	GPIO.cleanup()

# Function to start buzzer
def buzzer_init():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUZZER_PIN,GPIO.OUT)
	b = GPIO.PWM(BUZZER_PIN,1190)
	b.start(50)
	return b

# Function to capture image from camera
def capture_image(cam):
	img = cam.getImage()
	if(img): return img
	print "Could not get image\n"
	return False
	
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

# Function that returns blobs of a certain RGB color from an image
def color_check(img, color, tol=BIN_TOLERANCE):
	c = img.colorDistance(color)
	b = c.binarize(tol)
	blobs = img.findBlobsFromMask(b)
	if blobs:
		return blobs
	else: return 0

# An attempt to speed up the tarp-finding algorithm
#supposed to replace color_check if it works
def color_check_helper(img, color1, color2, color3, tol=COLOR_TOLERANCE):    #this new function takes in all 3 colors and the tolerance
	#imgcopy = []
	x = 0
	y = 0
	while(x<img.size()[0]): #iterate int x across the width
		y = 0
		while(y<img.size()[1]): #iterate int y across the height
			RGB = img[x,y] #RGB is of type integer tuple with 3 values
			distance1 = distance3d(RGB,color1) <= tol
			distance2 = distance3d(RGB,color2) <= tol
			distance3 = distance3d(RGB,color3) <= tol
			if distance1 or distance2 or distance3:
				img[x, y] = (255, 255, 255)   #pixels within tarp tolerance are changed to pure white
			else:
				img[x, y] = (0, 0, 0)   #pixels out of any color range are colored pure black
			y += 1
		x += 1
	return img

# Function to find distance between two 3d tuples
def distance3d(p1,p2):
	d = math.sqrt( math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2) + math.pow(p1[2]-p2[2],2))
	return d

# Function to draw blob outlines on given image's drawing layer
def draw_blobs(img, blobs, color):
	if(blobs):
		for blob in blobs:
			blob.drawOutline(color,width=4,layer=img.dl())

# Function that filters blobs based on being approximately a rectangle
def filter_rects(blobs, tol=RECT_TOLERANCE):
	if(blobs):
		rects = blobs.filter([b.isRectangle(tol) for b in blobs])
		return rects
		
# Function that filters blobs based on size
def filter_size(blobs,min_size=SIZE_MIN,max_size=SIZE_MAX):
	size = blobs.filter([(b.area() < max_size and b.area() > min_size) for b in blobs])
	return size

# Function that returns the blobs of possible tarps from an image
def find_tarps(img):
	tarps = [color_check(img,RED), color_check(img,BLUE), color_check(img,YELLOW)]
	#tarps = color_check_helper(img, RED, BLUE, YELLOW)
	return tarps
	
# Function to get the max and min sizes of the tarps in pixels
def get_size():
	##TODO: write function
	return False

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
def save_image(img,t,with_dl=False):
	write_log(t+", image saved")
	img.save(DIRECTORY+IMAGE_NAME+t+IMAGE_TYPE)
	if(with_dl):
		img.dl().clear()
		img.save(DIRECTORY+IMAGE_NAME+t+"_nodl"+IMAGE_TYPE)
	return 1

# Function to save image with custom name	
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
