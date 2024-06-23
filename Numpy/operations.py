import numpy as np

lista = [1,2]

print(lista * 2)

arr= np.arange(0,10)
arr_2 = arr.copy()

#Operations

#Multiplication
print (arr * 2)

#sum
print(arr + 2)

#division
print(1/arr)

#elevar al cuadraro
print(arr ** 2)

#Sum of arrays
print(arr + arr_2)

matriz = arr.reshape(2,5)
print(matriz)

matriz_2 = matriz.copy()

print(matriz + matriz_2)

#Producto punto
print(np.matmul(matriz, matriz_2.T))

print('\n Option 2', matriz @ matriz_2.T)

