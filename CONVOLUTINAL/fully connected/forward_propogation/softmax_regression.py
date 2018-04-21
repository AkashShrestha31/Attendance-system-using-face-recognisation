import numpy as np
def softmax_Regression(Z):
	t=np.round(np.exp(Z),2)
	sum_t=np.sum(t)
	a=[(i/sum_t) for i in t]
	a=np.round(a,3)
	print(a)
