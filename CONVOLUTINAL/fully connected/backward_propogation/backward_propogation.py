from backward_propogation import relu_back
def backward_propogation(dA,cache,activation):
	linear_cache,A=cache
	if activation=="relu":
		dZ=relu_back(dA,A)
		dW,db,dA=linear_cache(dZ,linear_cache)

	if activation=="sigmoid":
		dZ=relu_back(dA,A)
		dW,db,dA=linear_cache(dZ,linear_cache)
	return dW,db,dA