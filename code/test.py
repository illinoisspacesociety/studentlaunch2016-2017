from main import *
from SimpleCV import *
#import time
from datetime import *

test_rect = 0
test_tolerances = 0
test_pic_time_1080 = 1
test_pic_time_max = 1
#print time.now()

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
		
if(test_pic_time_1080):
	width = 1920
	height = 1080
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("1920x1080")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print t
		write_log(t)

if(test_pic_time_max):
	width = 3280
	height = 2464
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("1920x1080")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print t
		write_log(t)
