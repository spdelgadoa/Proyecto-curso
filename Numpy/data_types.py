import numpy as np 

arr = np.array([1,2,3,4], dtype='float64')
arr.dtype
print(arr.dtype)
print(arr)

#Change to bool

arr = np.array([0,1,2,3,4])
arr = arr.astype(np.bool_)
print('\n To bool \n', arr)

#change to string
arr = np.array([0,1,2,3,4])
arr = arr.astype(np.string_)
print('\n To string \n', arr)

#change to int8
arr = np.array(['hola','0','1','2','3','4'])
arr = arr.astype(np.int8)
print('\n To int8 \n', arr)