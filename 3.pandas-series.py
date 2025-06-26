import pandas as pd
import numpy as np

# Creating a Series
# A Series is a one-dimensional labeled array capable of holding any data type
# (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively
# referred to as the index. The basic method to create a Series is to call:
# pd.Series(data, index=index)
# print(pd.__version__)

# membuat series 
# print(pd.Series([1, 2, 3, 4, 5]))

# hewan = pd.Series(['kucing', 'anjing', 'ikan', 'burung'])
# print(hewan)

# indexing
arr = np.array([10, 20, 30, 40, 50])
ser = pd.Series(arr)
# print(ser[2])

# data frame 
data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
index = ['a', 'b', 'c']
columns = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(data, index=index, columns=columns)
# print(df)

# melalu array numpy
dataRandom = np.random.randint(1, 100, size=(5, 5))
dfRandom = pd.DataFrame(dataRandom, index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
# print(dfRandom)

# melalui dictionary yang bervalue list
kendaraan = {
    'mobil': ['avanza', 'xenia', 'brio'],
    'motor': ['beat', 'vixion', 'cbr'],
    'sepeda': ['polygon', 'thrill', 'brompton']
}
# print(pd.DataFrame(kendaraan, index=index))

# melalui list yang berisi dictionary
dataKaryawan = [
    {'nama': 'Budi', 'usia': 30, 'jabatan': 'Manager'},
    {'nama': 'Siti', 'usia': 25, 'jabatan': 'Staff'},
    {'nama': 'Joko', 'usia': 28, 'jabatan': 'Supervisor'}
]
dfKaryawan = pd.DataFrame(dataKaryawan)
# print(dfKaryawan)

# Dataframe
# DataFrame adalah struktur data dua dimensi yang dapat menyimpan data dalam bentuk tabel
# dengan baris dan kolom. DataFrame dapat dianggap sebagai kumpulan dari beberapa Series yang
# memiliki indeks yang sama. DataFrame dapat dibuat dari berbagai sumber data seperti array, list,
# dictionary, atau file CSV. Untuk membuat DataFrame, kita dapat menggunakan fungsi pd.DataFrame(data, index=index, columns=columns).

dataKendaraan = {
    'Merek': ['Toyota', 'Honda', 'Suzuki'],
    'Model': ['Avanza', 'Civic', 'Swift'],
    'Tahun Produksi': [2020, 2019, 2021],
    'Tipe': ['MPV', 'Sedan', 'Hatchback']
}

indexKendaraan = ['A', 'B', 'C']
df_kendaraan = pd.DataFrame(dataKendaraan, index=indexKendaraan)
# print(df_kendaraan)
# mengakses kolom series
# print(df_kendaraan['Merek'])  # Mengakses kolom 'Merek'
# mengakses kolom dataframe
# print(df_kendaraan[['Merek', 'Tipe']])  # Mengakses kolom 'Merek'
# mengakses baris dengan index
# print(df_kendaraan.loc['A'])  # Mengakses baris dengan index 'A'
# mengakses baris dengan urutan index
# print(df_kendaraan.iloc[0])  # Mengakses baris pertama

# Mengakses isi dataFrame (indexing dan slicing)
# print(df_kendaraan.loc['C', 'Model'])
# print(df_kendaraan.iloc[2, 1])  # Mengakses .drop(columns=['Tahun Produksi'], inplace=True)
# print(df_kendaraan)baris kedua, kolom ketiga
# mengakases beberapa baris dan kolom
# print(df_kendaraan.loc[['A', 'B'], ['Merek', 'Tahun Produksi']])  # Mengakses baris A dan B, kolom Merek dan Tahun Produksi

# Mengubah nama kolom, index, dan isi DataFrame
df_kendaraan.rename(columns={'Merek': 'Brand', 'Model': 'Type'}, inplace=True)

# merubah baris / index
df_kendaraan.rename(index={'A': 'Kendaraan1', 'B': 'Kendaraan2', 'C': 'Kendaraan3'}, inplace=True)
# print(df_kendaraan)

# tambah coloumn warna
warna = ['Merah', 'Biru', 'Hijau']
df_kendaraan['Warna'] = warna
# print(df_kendaraan)

# menambahkan baris baru
# data_baru = {'Brand': 'Nissan', 'Type': 'X-Trail', 'Tahun Produksi': 2022, 'Tipe': 'SUV', 'Warna': 'Hitam'}
# df_kendaraan.loc['Kendaraan4'] = data_baru
# print(df_kendaraan)

# menghapus kolom
# df_kendaraan.drop(columns=['Tahun Produksi'], inplace=True)
# print(df_kendaraan)

# Menggabungkan DataFrame
# menggunakan concat
data_kendaraan_lain = {
    'Brand': ['BMW', 'Mercedes'],
    'Type': ['X5', 'C-Class'],
    'Tahun Produksi': [2021, 2020],
    'Tipe': ['SUV', 'Sedan'],
    'Warna': ['Putih', 'Hitam'] 
}
df_kendaraan_lain = pd.DataFrame(data_kendaraan_lain, index=['Kendaraan5', 'Kendaraan6'])
df_kendaraan_gabungan = pd.concat([df_kendaraan, df_kendaraan_lain])
print(df_kendaraan_gabungan)



