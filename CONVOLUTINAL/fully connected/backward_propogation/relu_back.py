import numpy as np
def relu_back(dA,Z):
	dZ=np.Zeros((Z.shape[0],Z.shape[1]))
	for i in range(Z.shape[0]):
		for j in range(Z.shape[1]):
			dZ[i,j]=0 if Z[i,j] <0 else 1
	return  np.multiply(dA,dZ)


