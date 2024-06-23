import numpy as np 
list(range(0,10))

np.arange(0,20)
print(np.arange(0,20))

print(np.zeros(3))

print(np.zeros((10,10)))

print(np.ones((10,5)))

#crear 100 valores entre 0 y 10
print(np.linspace(0,10,100))

#Crear matriz con diagonal en 1
print(np.eye(4))

#Generate random

print(np.random.rand(4))


print(np.random.rand(4,4))

print(np.random.randint(1,15))

#Valores enteros de 1 a 100, con una estructura de 10*10
print(np.random.randint(1,100,(10,10)))