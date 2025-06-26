import numpy as np

# cek numpy version
# print(np.__version__)

# latihan 1
a = [1, 2, 3, 4]
b = [[1, 2], [3, 4]]
# print(np.array(a)) # convert list to array
# print(np.array(b).shape) # convert list of list to array

# membuat array berdasarkan value menggunakan zeros, ones, full
a = np.zeros((2, 3)) # array 2x3 berisi 0
# print(a)

b = np.ones((2, 3)) # array 2x3 berisi 1
# print(a)

c = np.full((2, 3), 5) # array 2x3 berisi 5
print(c)

# linespace dan range
a = np.linspace(0, 1, 5) # array 1x5 dari 0 sampai 1
# print(a)

b = np.arange(0, 10, 2) # array 1x5 dari 0 sampai 10 dengan step 2
# print(b)

# bilangan genap sampai 100
a = np.arange(0, 100, 2) # array 1x50 dari 0 sampai 100 dengan step 2
# print(a)

arr_contoh = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_contoh[0, 0] = 100 # mengubah nilai array
print(arr_contoh)