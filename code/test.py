from main import *
from SimpleCV import *
import time
from datetime import datetime, timedelta

test_rect = 0
test_blob_time = 0
test_tolerances = 0
test_pic_time_1080 = 0
test_pic_time_max = 0
test_blob_colors = 0
test_color_matching = 0
test_drawing_layer = 0
test_color_video = 0
test_parameters = 0
test_edges = 0
test_blob_on_edge = 0
test_binarize = 0
test_color_distance = 0
test_color_distance2 = 0
test_new_main = 1
test_color_check_helper = 0
test_color_access = 0
test_i2c = 0

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Show rectangles in pic
if(test_rect):
	#cam = SimpleCV.Camera()
	#img = capture_image(cam)
	img = Image("test_images/test11.png")
	rects = find_rects(img, 0.4)
	for rect in rects:
		rect.drawOutline((128,0,0),-1,4)
	save_image(img)
	time.sleep(3)
	
# Logs the time to find rectangles in image
if(test_blob_time):
	width = 1920
	height = 1080
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	write_log("\nFinding Rectangles\n")
	i = 0
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		rects = find_rects(img, float(i)/100)
		i += 1
		for rect in rects:
			rect.drawOutline((128,0,0),-1,4)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print i
		print t
		write_log(t)
	

#Saves 100 versions of test file showing various tolerances of blobs rect
if(test_tolerances):
	i = 0
	while(i<100):
		img = Image("test_images/test11.png")
		rects = find_rects(img, float(i)/100)
		for rect in rects:
			rect.drawOutline((128,0,0),-1,4)
		save_image(img)
		i += 1
		
#Logs time to take and save a 1920x1080 pic
if(test_pic_time_1080):
	width = 1280
	height = 720
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("\n1920x1080\n")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		#blobs = img.findBlobs()
		#for blob in blobs:
		#	blob.drawOutline((128,0,0),-1,4)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print t
		write_log(t)
		i += 1
		
#Logs time to take and save a 3280x2464 pic
if(test_pic_time_max):
	width = 3280
	height = 2464
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("\n3280x2464\n")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		blobs = img.findBlobs()
		for blob in blobs:
			blob.drawOutline((128,0,0),-1,4)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print i
		print t
		write_log(t)
		i += 1

#Prints the colors of blobs in a pic
if(test_blob_colors):
	img = Image("test_images/test11.png")
	rects = find_rects(img)
	for rect in rects:
		print rect.meanColor()
		print check_color2(rect,(100,100,100))

#Tests if blobs color near target		
if(test_color_matching):
	print "testing"
	
if(test_drawing_layer):
	img = Image("test_images/test2.png")
	dl = img.dl()
	rects = find_rects(img)
	for rect in rects:
		rect.drawOutline(color=(128,0,0),width=4,layer=dl)
	img.save("/home/asa/Documents/StudentLaunch/wdl.png")
	#img = Image("/home/asa/Documents/StudentLaunch/wodl.png")
	img.dl().clear()
	img.save("/home/asa/Documents/StudentLaunch/wodl.png")

if(test_color_video):
	width = 1280
	height = 720
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	while(1):
		img = capture_image(cam)
		rects = find_rects(img)
		for rect in rects:
			if(check_color(rect,(0,0,255))):
				rect.drawOutline((128,0,0),-1,4)
				print rect.meanColor()
		img.show()

#Iterates over possible parameter values for finding blobs		
if(test_parameters):
	img = Image("test_images/test15.png")
	i = 0
	#while(i < 100):
		#blobs = img.findBlobs(threshval=float(i)/100)
		#draw_blobs(img,blobs)
		#save_test_image(img,"thresh=%f" % (float(i)/100))
		#i += 1
	i = 3
	j = 480/4
	k = 640/4
	l = 640/2
	while(i < 480):
		while(j < 640/2):
			#while(k < 4*640/5):
				#while(l < 4*640/5):
					blobs = img.findBlobs(threshval=-1, minsize=j, maxsize=640-j, threshblocksize=i, threshconstant=0)
					if blobs:
						draw_blobs(img,blobs)
						save_test_image(img,"min="+str(j)+"_max="+str(640-j)+"_block="+str(i))
					img.dl().clear()
					#l += 1
					#print "l: " + l
				#l = 0
				#k += 1
				#"k: " + k
			#k = 0
					j += 2
					print "i: "+str(i)+" j: "+str(j)
		j = 480/4
		i += 4
		#print "i: " + str(i)
	print "Done\n"
	
if(test_edges):
	img = Image("test_images/test17.png")
	i=0
	j=100
	while(i < 100):
		j = 100
		i += 1
		while(j > i):
			img = Image("test_images/test14.png")
			edge = img.edges(i,j)
			save_test_image(edge,"j="+str(j)+"_i="+str(i))
			print "i: "+str(i)+" j: "+str(j)
			j -= 1
	save_test_image(img,"image")

if(test_blob_on_edge):
	img = Image("test_images/test18.png")
	edge = img.edges(60,61)
	save_test_image(edge,"edge")
	blobs = edge.findBlobs(threshval=-1, minsize=1280/7, maxsize=1280/4, threshblocksize=0, threshconstant=0)
	draw_blobs(edge,blobs)
	save_test_image(edge,"blobs")
	img.dl().clear()
	blobs = img.findBlobsFromMask(edge)
	draw_blobs(img,blobs)
	save_test_image(img,"test")

if(test_binarize):
	img = Image("test_images/test18.png")
	img_copy = img
	i = 0
	j = 5
	while(i<1000):
		j = 5
		while(j<255):
			img_copy = img
			bina = img_copy.binarize(blocksize=i,p=j)
			save_test_image(bina,"bin_i="+str(i)+"_j="+str(j))
			blobs = img.findBlobsFromMask(bina)
			if blobs: 
				draw_blobs(img,blobs)
				save_test_image(img,"img_i="+str(i)+"_j="+str(j))
			print "i="+str(i)+" j="+str(j)
			img.dl().clear()
			j += 5
		if(i==0): i=1
		i += 10
	
if(test_color_distance):
	blue = (0,0,255)
	red = (255,0,0)
	yellow = (255,255,0)
	
	i = 0
	while(i<1):
		t1 = datetime.now()
		
		img = Image("test_images/test19.png")
		color = img.colorDistance(blue)
		save_test_image(color,"blue_search")
		save_test_image(color,"blue_inverse_"+str(i))
		bina = color.binarize(140)
		save_test_image(bina,"blue_bin_"+str(i))
		blobs = img.findBlobsFromMask(bina)
		if blobs:
			draw_blobs(img,blobs)
			save_test_image(img,"blue_blobs_"+str(i))
		i += 1
		print i
	
'''
		img = Image("test_images/test19.png")
		color = img.colorDistance(red)
		save_test_image(color,"red_search")
		inv = color.invert()
		save_test_image(inv,"red_inverse")
		bina = inv.binarize(125)
		save_test_image(bina,"red_bin")
		bin_inv = bina.invert()
		blobs = img.findBlobsFromMask(bin_inv)
		if blobs:
			draw_blobs(img,blobs)
			save_test_image(img,"red_blobs")
	
		img = Image("test_images/test19.png")
		color = img.colorDistance(yellow)
		save_test_image(color,"yellow_search")
		inv = color.invert()
		save_test_image(inv,"yellow_inverse")
		bina = inv.binarize(100)
		save_test_image(bina,"yellow_bin")
		bin_inv = bina.invert()
		blobs = img.findBlobsFromMask(bin_inv)
		if blobs:
			draw_blobs(img,blobs)
			save_test_image(img,"yellow_blobs")
		
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print t
		write_log(t)
'''

if(test_color_distance2):
	print "COLOR DISTANCE 2"
	i = 0
	j = 6
	while(j<22):
		i = 0
		j += 1
		print bcolors.OKGREEN + "STARTING PIC: " + str(j) + bcolors.ENDC
		while(i<255):
			tarps = [0,0,0]
			t1 = datetime.now()
			img = Image("test_images/live_tests/"+str(j)+".png")		
			imgB = img.copy()
			imgR = img.copy()
			imgY = img.copy()
		
			color = img.colorDistance(BLUE)
			save_test_image(color,"/blue/"+str(j)+"_blue_search")
			#inv = color.invert()
			#save_test_image(inv,str(j)+"_blue_inverse_")
			bina = color.binarize(i)
			save_test_image(bina,"/blue/bin/"+str(j)+"_blue_bin_"+str(i))
			tarps[0] = imgB.findBlobsFromMask(bina)
			draw_blobs(imgB,tarps[0],BLUE)
			save_test_image(imgB,"/blue/blobs/"+str(j)+"_blue_blobs_"+str(i))
			
			color = img.colorDistance(RED)
			save_test_image(color,"/red/"+str(j)+"_red_search")
			#inv = color.invert()
			#save_test_image(inv,str(j)+"_red_inverse_")
			bina = color.binarize(i)
			save_test_image(bina,"/red/bin/"+str(j)+"_red_bin_"+str(i))
			tarps[1] = imgR.findBlobsFromMask(bina)
			draw_blobs(imgR,tarps[1],RED)
			save_test_image(imgR,"/red/blobs/"+str(j)+"_red_blobs_"+str(i))
			
			color = img.colorDistance(YELLOW)
			save_test_image(color,"/yellow/"+str(j)+"_yellow_search")
			#inv = color.invert()
			#save_test_image(inv,str(j)+"_yellow_inverse_")
			bina = color.binarize(i)
			save_test_image(bina,"/yellow/bin/"+str(j)+"_yellow_bin_"+str(i))
			tarps[2] = imgY.findBlobsFromMask(bina)
			draw_blobs(imgY,tarps[2],YELLOW)
			save_test_image(imgY,"/yellow/blobs/"+str(j)+"_yellow_blobs_"+str(i))
			
			if(tarps):
				for idx, blobs in enumerate(tarps):
					if(blobs!=0):
						rects = find_rects(blobs,RECT_TOLERANCE)
						color = (0,0,0)
						if(idx==0): color = BLUE
						elif(idx==1): color = RED
						elif(idx==2): color = YELLOW
						draw_blobs(img,rects,color)
			save_test_image(img,"/blobs/"+str(j)+"_blobs_"+str(i))
			t2 = datetime.now()
			dt = t2 - t1
			t = str(dt.seconds*1000000 + dt.microseconds)
			print str(i)+": "+str(t)
			#write_log(t)
			i += 10
		
if(test_new_main):
	i = 0
	while(i<21): 
		img = Image("test_images/live_tests/"+str(i+1)+".png")
		size = get_size()
		#rects = find_rects(img)
		tarps = find_tarps(img)
		#draw_blobs(img, tarps)
		i += 1
		#if(check_success()):
		if(tarps):
			for idx, blobs in enumerate(tarps):
				if(blobs!=0):
					size = filter_size(blobs)
					rects = find_rects(size)
					color = (0,0,0)
					if(idx==0): color = RED
					elif(idx==1): color = BLUE
					elif(idx==2): color = YELLOW
					#if(rects): draw_blobs(img,blobs,color)
					draw_blobs(img,rects,color)
			save_test_image(img,"pic_"+str(i))
			print i
		
if(test_color_check_helper):
	i = 0
	while(i<255):
		img = Image("test_images/test19.png")
		img2 = color_check_helper(img,RED,YELLOW,BLUE,i)
		save_test_image(img2,"color_check_helper_"+str(i))
		i += 5
		print i
		
if(test_color_access):
	img = Image("test_images/test19.png")
	img2 = img.copy()
	rgb = img[0,0]
	print rgb
	color1 = RED
	color2 = BLUE
	color3 = YELLOW
	i = 0
	j = 0
	print img.size()[0]
	distance1 = math.sqrt(math.pow(rgb[0] - color1[0], 2) + math.pow(rgb[1] - color1[1], 2) + math.pow(rgb[2] - color1[2], 2)) <= COLOR_TOLERANCE
	while(i<img.size()[0]):
		j = 0
		while(j<img.size()[1]):
			img2[i,j] = (0,0,0)
			#print j
			j += 1
		i += 1
		print i
	print img2[0,0] 
	save_test_image(img2,"test")

if(test_i2c):
	bus = SMBus(1)
	address = 0x76
	cmd = 0x40
	press = 0
	#with I2CMaster() as master:
	#	press = master.transaction(writing_bytes(address,cmd),reading(address,1))
	#press = bus.read_block_data(address,0x00)
	#bus.write_byte_data(address,0,0x1E)
	#bus.write_byte_data(address,0,0x00)
	#pres = bus.read_i2c_block_data(address,0,3)
	
	#press1 = bus.write_byte_data(address,0,cmd)
	#press2 = bus.write_byte_data(address,0,0x00)
	#press2 = bus.read_byte_data(address,0)
	bus.write_byte(address,cmd)
	#press3 = bus.write_byte(address,0x00)
	press3 = bus.process_call(address,0x40,0)
	#print press1
	#print press2
	print press3
	bus.close()
