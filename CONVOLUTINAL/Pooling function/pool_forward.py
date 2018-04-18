import numpy as np


def pool_forward(A_prev,hparameters,mode="max"):
	#Retriving A_prev that return no of image,image heighnt,image width,image depth
	(m,n_H_prev,n_W_prev,n_C_prev)=A_prev.shape
	#retriving height , widht ,depth and no of filters
	
	f=hparameters['f']
	stride=hparameters['stride']
	n_H=int((n_H_prev-f)/stride)+1
	n_W=int((n_W_prev-f)/stride)+1
	n_C=n_C_prev
	#output volume z
	A=np.zeros((m,n_H,n_W,n_C))

	for i in range(m):
		
		for h in range(n_H):
			for w in range(n_W):
				for c in range(n_C):
					vert_start=h*stride
					vert_end=vert_start+f
					horiz_start=stride*w
					horiz_end=horiz_start+f
					a_slice_prev=A_prev[vert_start:vert_end,horiz_start:horiz_end,c]
					if mode=="max":
						A[i,h,w,c]=np.max(a_slice_prev)
					if mode=="average":
						A[i,h,w,c]=np.mean(a_slice_prev)
	cache=(A_prev,hparameters)
	return A,cache
np.random.seed(1)
hparameters={"f":4,
				"stride":1}
z,cache=pool_forward(np.random.randn(10,4,4,3),hparameters,mode='max')
print(z.shape)