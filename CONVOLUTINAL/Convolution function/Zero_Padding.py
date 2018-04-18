import matplotlib.pyplot as plt
import numpy as np
def zero_pad(X,pad):
	x_pad=np.pad(X,((0,0),(2,2),(2,2),(0,0)),'constant',constant_values=0)
	return x_pad

