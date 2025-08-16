import numpy as np

arr=np.array([[10,20,30],[40,50,60]])
print(arr.size)
print(arr.ndim) # no. of dimension
print(arr.dtype)

int_arr=arr.astype(int)
print(int_arr)
print(int_arr.dtype)
