def pooling_backward(dA,cache,mode="max"):
	A_prev,hparameters=cache
	m,n_H_prev,n_W_prev,n_C_prev=A_prev.shape
	stride=hparameters["stride"]
	f=hparameters["f"]
	dA_prev=np.zeros(A_prev.shape)
	m,n_H,n_W,n_C=dA.shape
	for i in range(m):
		for 


