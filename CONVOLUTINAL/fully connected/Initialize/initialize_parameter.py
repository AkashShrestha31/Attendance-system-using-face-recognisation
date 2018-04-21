import numpy as np
from scipy import ndimage
import matplotlib.pyplot  as plt
import scipy.misc
import numpy as np
def initialize_parameter(n_X,n_Y,n_h):
	parameters={}
	parameters["W1"]=np.random.randn(n_h,n_X)*0.01
	parameters["b1"]=np.zeros((n_h,1))
	parameters["W2"]=np.random.randn(n_Y,n_h)*0.01
	parameters["b2"]=np.zeros((n_Y,1))
	return parameters

