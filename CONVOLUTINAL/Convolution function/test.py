import cv2
import numpy as np
from numpy import *
import csv

obj=open("C:/Users/AK/Desktop/CONVOLUTINAL/color.csv", "r",)
np.random.seed(0)
file=csv.reader(obj)
for line in file:
	print("R",np.random.randint(0,155))
	print("G",np.random.randint(0,155))
	print(np.random.randint(0,155))
