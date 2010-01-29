#!/usr/bin/env python
#-*- coding:utf-8 -*-

import opencv.highgui

class Camera(object):
    """Class to manage getting, processing, and displaying video."""
    def __init__(self, width=640, height=480, camera=0, file=False):
        self.width = width
        self.height = height
        if file:
            self.capture = opencv.highgui.cvCreateFileCapture(file)
        else:
            self.capture = opencv.highgui.cvCreateCameraCapture(camera)
        
    def get_frame(self):
        """Get a frame from the Camera or Video"""
        return opencv.highgui.cvQueryFrame(self.capture)

    def process_frame(self, frame):
        """Process the frame"""
        # Just return the frame for now
        #TODO: Write real code here
        return frame

    def display_capture(self, fps = 30, window_name = "Camera"):
        """Display camera capture."""
        opencv.highgui.cvNamedWindow(window_name,
                                    opencv.highgui.CV_WINDOW_AUTOSIZE)
        
        while True:
            frame = self.process_frame(self.get_frame())
            opencv.highgui.cvShowImage(window_name, frame)
            waitkey = opencv.highgui.cvWaitKey(1000 / fps)
            if waitkey == "c":
                break

if __name__ == '__main__':
    webcam  = Camera()
    webcam.display_capture()

