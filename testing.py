#!/usr/bin/python
from opencv.cv import *
from opencv.highgui import *
import sys

def display_capture(capture):
    cvNamedWindow( "Testing", 1 )

    while True:
        frame = cvQueryFrame( capture )
        if not frame:
            cvWaitKey(0)
            break

        cvShowImage("Testing", process_frame(frame))

        if cvWaitKey(10) != -1:
            break

    cvDestroyWindow("Testing")

def process_frame(frame):
    return frame

if __name__ == "__main__":
    capture = None
    
    if len(sys.argv)==1:
        capture = cvCreateCameraCapture( 0 )
    elif len(sys.argv)==2 and sys.argv[1].isdigit():
        capture = cvCreateCameraCapture( int(sys.argv[1]) )
    elif len(sys.argv)==2:
        capture = cvCreateFileCapture( sys.argv[1] ) 

    if not capture:
        print "Could not initialize capturing..."
        raise SystemExit
    else:
        display_capture(capture)
