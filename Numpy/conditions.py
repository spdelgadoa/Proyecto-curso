import numpy as np

'''
arr = np.linspace(1,10,10, dtype='int8')
print(arr)
indices_cond = arr > 5
print(indices_cond)


print(arr[indices_cond])

print(arr[(arr > 5 )& (arr < 9 )])

arr[arr > 5] = 99

print(arr[arr==99])
'''
arr_2 = np.arange(0,200,5)

#RETO

arr = np.linspace(10,100, 40, dtype='int8')

print('Size', arr.size)
print(arr)
matriz = arr.reshape(5,8)
print('\n Matriz original ', matriz)

#Filter > 50 in matrix
case1 = matriz[matriz > 50]
print('\n Case 1 ', case1)

#Filter < 50 in matrix
case2 = matriz[matriz < 50]
print('\n Case 2 ', case2)

#Filter < 50 and Even
case3 = matriz[(matriz < 50)& (matriz % 2 ==0)]
print('\n Case 3 ', case3)

#Filter >50 and Odd
case4 = matriz[(matriz > 50)&(matriz%2!=0)]
print('\n Case 4 ', case4)
