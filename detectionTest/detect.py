import os
import glob
import time
from SimpleCV import *

#cam = SimpleCV.Camera()

path = os.getcwd()
ext = "*.bmp"
directory = os.path.join(path, ext)

img = Image("test.bmp")
blobs = img.findBlobs()
if blobs:
	blobs.draw(color=(0,0,0), width=10)
img.show()
time.sleep(2)
