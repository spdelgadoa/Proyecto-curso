import numpy as np 

arr = np.random.randint(1,20,10)

matriz = arr.reshape(2,5)
print(matriz)

#Max number
print(arr.max())
print(matriz.max(0))

#Which axis
print('\n By rows')
print(matriz.max(1))
print('\n By columns')
print(matriz.max(0))

print('\n index with the max number')
print(arr.argmax())

print('\n index with the max number in Matrix')
print(matriz.argmax(0))

#Min number
print('\n Func Min')

print(arr.min())
print(matriz.min(0))

#Which axis
print('\n By rows')
print(matriz.min(1))
print('\n By columns')
print(matriz.min(0))
print('\n index with the max number')
print(arr.argmin())

print('\n index with the max number in Matrix')
print(matriz.argmin(0))


#PickToPick
print('\n Distance Max to Min')
print(arr.ptp())

print('\n Matrix Distance Max to Min')
print(matriz.ptp(0))

#Percentil

print('\n Percentile 50')
print(np.percentile(arr,50))
print('\n Median', np.median(arr))

print('\n Median axis 0')
print(np.median(matriz,0))

print('\n ArrSDT')
print(np.std(arr))

print('\n Arr Var')
print(np.var(arr))

print('\n Arr Mean')
print(np.mean(arr))

print('\n Matrix SDT')
print(np.std(matriz,0))

#Sort
print('\n Sort')
print(np.sort(arr))

#Concatenate

a = np.array([[1,2],[3,4]])
print(a)
b = np.array([5,6])
#To match Dimensions
b = np.expand_dims(b, axis=0)
print(b)
print(b.T)

print('\n Concatenate A + B')
print(np.concatenate((a,b),axis=0))


print('\n Concatenate A + B')
#Error due to form of array
#print(np.concatenate((a,b),axis=1))
#Solutions - use transpose
print(np.concatenate((a,b.T),axis=1))
