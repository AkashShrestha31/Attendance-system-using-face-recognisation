import numpy as np
def linear_back(dZ,cache):
	A1,W,b=cache
	m=??
	dW=1/m*np.dot(dZ,A1)
	db=1/m*np.sum(dZ,axis=1,keepdims=True)
	dA=np.dot(W,dZ)
	return dW,db,dA