from main import *
from SimpleCV import *
import time

test_rect = 0
test_tolerances = 1

# Show rectangles in pic
if(test_rect):
	#cam = SimpleCV.Camera()
	#img = capture_image(cam)
	img = Image("test_images/test11.png")
	rects = find_rects(img)
	for rect in rects:
		rect.drawOutline((128,0,0),-1,4)
	img.show()
	time.sleep(3)
	
if(test_tolerances):
	#img = Image("test_images/test11.png")
	for i in range(0,100):
		img = Image("test_images/test11.png")
		rects = find_rects(img, i/100)
		for rect in rects:
			rect.drawOutline((128,0,0),-1,4)
			
