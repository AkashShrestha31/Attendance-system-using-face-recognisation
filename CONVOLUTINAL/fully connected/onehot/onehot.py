import numpy as np
def onehot(labels):
	x_one_hot=np.zeros((len(labels),len(labels)))
	for i in range(9):
			print()
			x_one_hot[i,x[i]-1]=1 
	print(x)
	print(x_one_hot)
# x=np.array([1,3,3,0,5,6,7,8,1])
# onehot(x)

