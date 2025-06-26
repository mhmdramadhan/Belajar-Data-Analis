import numpy as np

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print(np.add(arr_a, arr_b)) # penjumlahan
print(np.subtract(arr_a, arr_b)) # pengurangan
print(np.multiply(arr_a, arr_b)) # perkalian

arr_c = np.array([1,2,3,4,5,5])
# mencari rata rata
print(np.mean(arr_c)) # rata-rata

print(np.median(arr_c)) # median

print(np.std(arr_c)) # standar deviasi  