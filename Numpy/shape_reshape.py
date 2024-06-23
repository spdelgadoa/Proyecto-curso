import numpy as np 
'''
arr = np.random.randint(1,10,(3,2))
print(arr.shape)
print(arr)
#Cambia la forma de l array
print(arr.reshape(1,6))

#Reshape como lo hace el lenguaje "C"

print(np.reshape(arr,(2,3),'C'))

#Reshape en lenguaje Fortran
print(np.reshape(arr,(2,3),'F'))

#Reshape en lenguaje Aleatorio
print(np.reshape(arr,(2,3),'A'))
'''

#RETO

arr2 = np.random.randint(5,100,(2,5,8))
print(arr2)

#reshape
print(np.reshape(arr2,(4,2,10)))

#Reshape 2
print(np.reshape(arr2,(2,2,20)))

#Reshape error
#print(np.reshape(arr2,(5,4,8)))


