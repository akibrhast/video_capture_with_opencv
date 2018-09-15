import cv2
import numpy as np
import datetime, os

cam = cv2.VideoCapture(0)
path = os.getenv('APPDATA')+'/VideoCaptureChookie'

if not os.path.isdir(path):
   os.mkdir(path)


    
vid_counter = 1

start = datetime.datetime.now()
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('%s/%s.avi' % (path, start.strftime("%y-%m-%d-%H-%M-%S")),fourcc, 20.0, (640,480))

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret==True:

        # write the  frame
        out.write(frame)

        elapsed = datetime.datetime.now()-start
        if  elapsed > datetime.timedelta(seconds=5):
            vid_counter +=1
            if  vid_counter > 3:
                break
            start = datetime.datetime.now()
            out = cv2.VideoWriter('%s/%s.avi' % (path, start.strftime("%y-%m-%d-%H-%M-%S")),fourcc, 20.0, (640,480))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break
		


# Release everything if job is finished
cam.release()
out.release()
cv2.destroyAllWindows()

