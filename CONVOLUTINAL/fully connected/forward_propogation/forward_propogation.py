import numpy as np
def forward_propogation(A_prev,W,b,activation):
	if activation=="relu":
		Z=np.dot(A_prev,w)+b
		cache=(A_prev,w,b)
		A=relu(Z)
	if activation=="sigmoid":
		z=np.dot(A_prev,w)+b
		cache=(A_prev,w,b)
		A=sigm(Z)
	return cache,A

