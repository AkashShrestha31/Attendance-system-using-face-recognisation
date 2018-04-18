import numpy as np
np.random.seed(0)
x=np.random.randn(4,3,3,2)
x_pad=np.pad(x,((0,0),(2,2),(2,2),(0,0)),'constant',constant_values=0)
print(x_pad)