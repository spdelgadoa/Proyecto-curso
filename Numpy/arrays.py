import numpy as np 
lista = [1,2,3,4,5,6,7,8,9]

arr = np.array(lista)

type(arr)
print ('Este es esl tipo -->', type)
print (arr)
print(lista)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz_np = np.array(matriz)
print(matriz)

arr[0]
print(arr[0]+ arr[5])

matriz [0]
print(matriz_np[0,2])

arr[0:3]
print(arr[2:8])
#Traer de 3 en 3
print(arr[::3])
#from the end of the list
print(arr[-1])
print(arr[-3:])
print(arr[::-3])

#Matrix
print('---MATRIX from here ----')
print(matriz_np[1:])

#column level

print(matriz_np[:,2:3])

print(matriz_np[1:,0:2])
#Arreglo de 3D de la forma 2 x 3 x 4; 2 matrices (C/U 3 filas y 4 columnas)



#RETO


arreglo_3d = np.array([[[1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12]],

                       [[13, 14, 15, 16], 
                        [17, 18, 19, 20], 
                        [21, 22, 23, 24]]])
print('-----3D array-----')

'print(arreglo_3d)'
#1st row of each matrix
print('Rows: \n ',  arreglo_3d[0:2,0:2,0])

#1st column of each matrix
print('\n Columns: \n', arreglo_3d[:,:,3])