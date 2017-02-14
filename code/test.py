from main import *
from SimpleCV import *
import time

cam = SimpleCV.Camera()
#img = capture_image(cam)
img = Image("test2.png")
img = find_blobs(img)
img.show()
time.sleep(3)
