import sys
import cv2
from cv2 import *
import numpy as np
import sys


kernel_d = np.ones((3,3), np.uint8)	
kernel_e = np.ones((3,3), np.uint8)	
kernel_gauss = (3,3)	
dilate_times = 13
erode_times = 5
is_blur = True
is_close = True
is_draw_ct = False
fac = 2


def drawRectangle(frame, minus_frame):
	if(is_blur):
		minus_frame = GaussianBlur(minus_frame, kernel_gauss, 0)
	minus_Matrix = np.float32(minus_frame)	
	if(is_close):
		for i in range(dilate_times):
			minus_Matrix = dilate(minus_Matrix, kernel_d)
		imshow('dilate', minus_Matrix)
		for i in range(erode_times):
			minus_Matrix = erode(minus_Matrix, kernel_e)
		imshow('erode', minus_Matrix)
	minus_Matrix = np.clip(minus_Matrix, 0, 255)
	minus_Matrix = np.array(minus_Matrix, np.uint8)
	contours, hierarchy = findContours(minus_Matrix.copy(), RETR_TREE, CHAIN_APPROX_SIMPLE)
	for c in contours:
		(x, y, w, h) = boundingRect(c)	
		rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		if( is_draw_ct ):
			drawContours(frame, contours, -1, (0, 255, 255), 2)
	imshow('result', frame)

def objdetect():
	capture = VideoCapture(0);
	width = (int)( capture.get( CAP_PROP_FRAME_WIDTH )/fac )
	length = (int)( capture.get( CAP_PROP_FRAME_HEIGHT )/fac )
	while(1):
		(ret_old, old_frame) = capture.read()
		old_frame = resize( old_frame, ( width,length ),interpolation = INTER_CUBIC )
		gray_oldframe = cvtColor(old_frame, COLOR_BGR2GRAY)
		if(is_blur):
			gray_oldframe = GaussianBlur(gray_oldframe, kernel_gauss, 0)
		oldBlurMatrix = np.float32(gray_oldframe)
		accumulateWeighted(gray_oldframe, oldBlurMatrix, 0.003)
		while(True):
			ret, frame = capture.read()	
			frame = resize( frame, ( width,length ),interpolation = INTER_CUBIC )
			gray_frame = cvtColor(frame, COLOR_BGR2GRAY)
			if(is_blur):
				newBlur_frame = GaussianBlur(gray_frame, kernel_gauss, 0)
			else:
				newBlur_frame = gray_frame
			newBlurMatrix = np.float32(newBlur_frame)
			minusMatrix = absdiff(newBlurMatrix, oldBlurMatrix)
			ret, minus_frame = threshold(minusMatrix, 60, 255.0, THRESH_BINARY)
			accumulateWeighted(newBlurMatrix,oldBlurMatrix,0.02)
			imshow("difference", minus_frame)
			drawRectangle(frame, minus_frame)
			if cv2.waitKey(60) & 0xFF == ord('q'):
				break
		capture.release() 
		cv2.destroyAllWindows()
