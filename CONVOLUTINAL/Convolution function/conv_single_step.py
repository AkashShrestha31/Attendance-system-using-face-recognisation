import numpy as np
def conv_single_step(a_slice_prev,w,b):

	res=np.multiply(a_slice_prev,w)+b
	res=np.sum(res)
	return res