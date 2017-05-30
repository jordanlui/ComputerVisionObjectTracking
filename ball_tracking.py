# Import stuff

from collections import deque
import numpy as numpy
import argparse, imutils, cv2

# Argument parse construction, parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b","--buffer",type=int,default=64,help="max buffer size")
args = vars(ap.parse_args())

# Color thresholding for the object we're tracking
# Initialize lisit of tracked points