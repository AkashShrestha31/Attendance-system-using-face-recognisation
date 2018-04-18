import numpy as np
def sigmoid_back(dA,Z):
	dZ=np.multiply(dA,np.multiply(Z,(1-Z)))
	return dZ