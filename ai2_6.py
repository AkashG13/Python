import numpy as np
z= np.random.random((10,3))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(z)
print("__________________________________________\n ")
print(r)
print(t)
