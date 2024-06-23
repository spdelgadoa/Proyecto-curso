import numpy as np 

scalar = np.array(42)
print(scalar)
print(scalar.ndim)

vector = np.array([1,2,3])
print("\n", vector)
print(vector.ndim)


matrix = np.array([[1,2,3], [4,5,6]])
print("\n", matrix)
print(matrix.ndim)

tensor = np.array([[[1,2,3], [4,5,6],[7,8,9],[0,2,45]],[[1,2,3], [4,5,6],[7,8,9],[0,2,45]]])
print("\n", tensor)
print(tensor.ndim)

#Agregar o eliminar dimensiones

vector = np.array([1,2,3], ndmin=10)
print("\n", vector)
print(vector.ndim)

expand = np.expand_dims(np.array([1,2,3]), axis=0)
print(expand)
print(expand.ndim)

print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)