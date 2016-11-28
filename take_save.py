import SimpleCV

directory = "/home/asa/Documents/StudentLaunch/"
img_name = "test_image_"

cam = SimpleCV.Camera()
i = 0
while True:
	img = cam.getImage()
	img.save(directory+img_name+str(i)+".png")
	i = i+1
	break #take out to continually take and save images

