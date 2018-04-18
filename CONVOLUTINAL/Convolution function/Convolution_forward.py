import numpy as np
from Zero_Padding import *
from conv_single_step import *
def Convolution_forward(A_prev,W,b,hparameters):
	#Retriving A_prev that return no of image,image heighnt,image width,image depth
	(m,n_H_prev,n_W_prev,n_C_prev)=A_prev.shape
	#retriving height , widht ,depth and no of filters
	(f,f,n_C_prev,n_C)=W.shape
	pad=hparameters['pad']
	stride=hparameters['stride']
	n_H=int((n_H_prev-f+2*pad)/stride)+1
	n_W=int((n_W_prev-f+2*pad)/stride)+1
	#output volume z
	z=np.zeros((m,n_H,n_W,n_C))
	A_prev_pad=zero_pad(A_prev,pad)

	for i in range(m):
		a_prev_pad=A_prev_pad[i]
		for h in range(n_H):
			for w in range(n_W):
				for c in range(n_C):
					vert_start=h*stride
					vert_end=vert_start+f
					horiz_start=stride*w
					horiz_end=horiz_start+f
					a_slice_prev=a_prev_pad[vert_start:vert_end,horiz_start:horiz_end,:]
					z[i,h,w,c]=conv_single_step(a_slice_prev,W[...,c],b[...,c])
	cache=(A_prev,w,b,hparameters)
	return z,cache
np.random.seed(1)
hparameters={"pad":2,
				"stride":1}
z,cache=Convolution_forward(np.random.randn(10,4,4,3),np.random.randn(2,2,3,8),np.random.randn(1,1,1,8),hparameters)
print(z.shape)