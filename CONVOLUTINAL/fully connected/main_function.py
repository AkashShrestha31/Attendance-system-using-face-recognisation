from backward_propogation import *
from forward_popogation import *
from onehot import *
from initalize_parameter import *
from prepare_dataset import *
def main_function():
	X=prepare_dataset()
	parameters=initalize_parameter()
	for i in range(25):
		cache,A1=forward_popogation(X,parameters["W1"],parameters["b1"],"relu")
		cache2,A2=forward_popogation(A1,parameters["W2"],parameters["b2"]."sigmoid")

main_function()