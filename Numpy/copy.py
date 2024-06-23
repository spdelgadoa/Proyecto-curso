import numpy as np

arr = np.arange(0,11)
trozo_de_arr = arr[0:6]
trozo_de_arr[:] = 0
print(trozo_de_arr) 
print(arr)

arr_copy = arr.copy()

arr_copy[:] = 100

print(arr_copy)