#!/usr/bin/python

import opencv.cv
import camera

class Camera(camera.Camera):
    """docstring for Camera"""
    def __init__(self):
        super(Camera, self).__init__()

    def process_frame(self, frame):
#        opencv.cv.cvGoodFeaturesToTrack(frame, frame, 20, 0.1, 5, 3, False)
        print "test"
        return frame

if __name__ == '__main__':
    webcam = Camera()
    webcam.display_capture()
