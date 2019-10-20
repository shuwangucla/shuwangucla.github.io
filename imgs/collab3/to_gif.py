import cv2
import os
import numpy as np
import shutil

rt = os.getcwd()
files = os.listdir()
for f in files:
	if f[-3:] == "mp4":
		filename = f
		cap = cv2.VideoCapture(filename)
		property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
		length = int(cv2.VideoCapture.get(cap, property_id))
		tot_time = 10.0
		speed = tot_time/(length/25)
		os.system("ffmpeg -y -r 25 -i " + filename + " -f gif -r 25 -s 500x500 " + "-filter:v \"setpts="+ str(speed) +"*PTS\" " + filename[0:-4]+"_rescale.gif")
		os.remove(filename)

