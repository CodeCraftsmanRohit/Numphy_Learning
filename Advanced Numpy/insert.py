'''

np.insert(array,index,vaue,axis=None)
array-original array
index-
value-
axis-
axis=0  ->row-wise   , axis=1 -> column-wise


'''
import numpy as np

arr=np.array([10,20,30,40,50,60])
print(arr)
new_arr=np.insert(arr,2,100)
print(new_arr)