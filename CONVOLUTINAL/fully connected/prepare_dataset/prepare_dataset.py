# 	path="C:/Users/AK/Desktop/attendance system using github/CONVOLUTINAL/capture/capture102.jpg"
# 	image=np.array(ndimage.imread(path))
# 	my_image = scipy.misc.imresize(image, size=(64, 64,3))
# 	print(image.shape)
# 	plt.imshow(my_image)
# 	plt.show()
# 	plt.imshow(image)
# 	plt.show()
# prepare_dataset()
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import fully connected.onehot
def prepare_dataset():
	
	path="C:/Users/AK/Desktop/attendance system using github/CONVOLUTINAL/Dataset/train.csv"
	x=genfromtxt(path,delimiter=',')
	no_of_train,fetures=x[1:,1:].shape
	X =x[1:,1:]#np.zeros((no_of_train,fetures))
	Y =x[1:,0:1]#np.zeros((no_of_train,10))
	Y=onehot(Y.T)
	print(X.shape)
	print(Y.shape)
prepare_dataset()
