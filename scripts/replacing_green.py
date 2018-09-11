import cv2
import numpy as np

image = cv2.imread('./green.jpg')

green_range = np.array([[0,50,0], [125,255,125]])
