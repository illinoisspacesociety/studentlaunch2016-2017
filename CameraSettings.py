#Script to possibly display camera settings
from SimpleCV import *

with cam.Camera() as camera:
	res = camera.resolution
	rate = camera.framerate
	shutter = camera.shutter_speed
	expose = camera.exposure_speed
	expose_mode = camera.exposure_mode
	awb_gains = camera.awb_gains
	awb_mode = camera.awb_mode
	
print('Camera Settings')
print('Resoultion:\t'+res)
print('Framerate:\t'+rate)
print('Shutter Speed:\t'+shutter)
print('Exposure Speed:\t'+expose)
print('Exposure Mode:\t'+expose_mode)
print('AWB Gains:\t'+awb_gains)
print('AWB Mode:\t'+awb_mode)