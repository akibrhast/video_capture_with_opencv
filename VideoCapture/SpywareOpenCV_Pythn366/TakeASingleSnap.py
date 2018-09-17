import cv2
import numpy
from constants import *
import datetime, os



def main(cam):
	
	#Ensures everything is saved in the same directory
	if not os.path.isdir(VIDEO_DIRECTORY_PATH):
		os.mkdir(VIDEO_DIRECTORY_PATH)
	
	#Date Time Counter to append to filename
	start=datetime.datetime.now()

	if(cam.isOpened() and cv2.waitKey(1) & 0xFF == ord('y')):
		cv2.imwrite('%s/%s.png'%(VIDEO_DIRECTORY_PATH,start.strftime("%y-%m-%d-%H-%M-%S")),frame)

if __name__ == '__main__':
    main(cam)