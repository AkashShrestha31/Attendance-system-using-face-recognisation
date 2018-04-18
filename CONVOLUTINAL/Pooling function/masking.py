import numpy as np
def create_mask_from_window(x):
	X=x==np.max(x)
	return X

