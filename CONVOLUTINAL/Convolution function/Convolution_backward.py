import numpy as np
def Convolutional_backward(dZ,cache):
	A_prev,W,b,hparameters=cache

	m,n_H_prev,n_W_prev,n_C_prev=A_prev.shape

	f,f,n_C_prev,n_C=W.shape

	stride=hparameters["stride"]
	pad=hparameters["pad"]
	m,n_H,n_W,n_C=dz.shape

	dA_prev=np.zeros((m,n_H_prev,n_W_prev,n_C_prev))
	dW=np.zeros((f,f,n_C_prev,n_C))
	db=np.zeros((1,1,1,n_C))

	A_prev_pad=zero_pad(A_prev,pad)
	dA_prev_pad=zero_pad(dA_prev,pad)

	for i in range(m):
		A_prev_pad=A_prev_pad[i]
		da_prev_pad=dA_prev_pad[i]
		for h in range(n_H):
			for w in range(n_W):
				for c in range(n_C):
					vert_start=h
					vert_end=vert_start+f
					horiz_start=w
					horiz_end=horiz_start+f
					a_slice=A_prev_pad[vert_start:vert_end,horiz_start:horiz_end,:]
					da_prev_pad[vert_start:vert_end,horiz_start:horiz_end,:]+=W[:,:,:,c]*dZ[i,h,w,c]
					dW[:,:,:,c]+=a_slice*dZ[i,h,w,c]
					db[:,:,:,c]+=dZ[i,h,w,c] 
		dA_prev[i,:,:,:]=da_prev_pad[pad:-pad,pad:-pad,:]
	return dA_prev,dW,db