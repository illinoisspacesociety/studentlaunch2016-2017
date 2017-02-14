#!/usr/bin/python

import SimpleCV

LOAD_IMG = "/detectionTest/rectTest.png"

def main():
	img = get_img()
	img.show()
	return

def get_img():
	img = Image(LOAD_IMG)
	return img

if __name__ == "__main__":
    main()
