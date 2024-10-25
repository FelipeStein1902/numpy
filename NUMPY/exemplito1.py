import numpy as np

lista_normal = [5, 3.5,2 ,8 ,9]

array = np.array(lista_normal, dtype=int)

print(lista_normal)
print(type(lista_normal))
print(array)
print(type(array))
print(array.dtype)

#Dimensions

ar1 = np.array(42) #0 DIMENSÕES
print(ar1)
print(ar1.ndim)

ar2 = np.array([1,2,3]) #1 DIMENSÃO
print(ar1)
print(ar1.ndim)

ar3 = np.array([   #2 DIMENSÕES
    [1,2,3],
    [4,5,6]
]) 
print(ar3)
print(ar3.ndim)

ar4 = np.array([   #3 DIMENSÕES
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])  
print(ar4)
print(ar4.ndim)

#index
ar5 = np.array([1,2,3])

print(ar5)
print(ar5.ndim)
print(ar5[1])

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr[1,2])

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr[1,-1,1])