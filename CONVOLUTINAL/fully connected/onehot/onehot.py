import numpy as np
def onehot(labels):

	x_one_hot=np.zeros((len(labels),np.max(labels)+1))
	print(x_one_hot.shape)
	for i in range(len(labels)):
			print(i)
			x_one_hot[i,labels[i]]=1 
	return x_one_hot

