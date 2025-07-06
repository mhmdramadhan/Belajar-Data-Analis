import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# cleaning data
data = {
    'A' : [1, 2, 3, 11],
    'B' : [4, None, 6, 7],
    'C' : [None, 10, None, 12],
    'D' : [13, 14, 11, 16]
}

df = pd.DataFrame(data)

# print(df)

# mengetahui data kosong
# print(df.isnull())

# menghitung jumlah data kosong
# print(df.isnull().sum())

# mengatasi data kosong
# menghapus kolom/baris data 
# df.dropna(axis=0, inplace=True)  # axis=0 untuk baris, axis=1 untuk kolom 
# print(df)
# df.dropna(axis=1, inplace=True)  # menghapus kolom yang memiliki data kosong
# print(df)

# mengisi data kosong
df.fillna(df.mean(), inplace=True)  # mengisi data kosong dengan 0
# print(df)

# mengisi data kosong dengan nilai sebelumnya dan sesudahnya
# df.fillna(method='ffill', inplace=True)  # mengisi data kosong dengan nilai sebelumnya
# df.fillna(method='bfill', inplace=True)  # mengisi data kosong dengan nilai sesudahnya
# print(df)


data2 = {
    'A' : [1, 2, None, 5],
    'B' : [1,2,3,4],
    'C' : [1,2,3,None],
    'D' : [None, 2,3,4]
}

df2 = pd.DataFrame(data2)

# menggunakan interpolate untuk mengisi data kosong
df2.interpolate(method='linear', inplace=True)  # mengisi data kosong dengan interpolasi   
# print(df2)

# menggunakan library missingno untuk visualisasi data kosong
df_pokemon = pd.read_csv('sample_data/Pokemon.csv')

 # menampilkan bar chart dari data kosong
msno.bar(df_pokemon, figsize=(10, 5), color='blue', fontsize=12)

msno.matrix(df_pokemon)
plt.show()