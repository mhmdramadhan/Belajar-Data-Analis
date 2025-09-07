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
# msno.bar(df_pokemon, figsize=(10, 5), color='blue', fontsize=12)

# msno.matrix(df_pokemon)
# plt.show()

data_double = {
    'A' : [1, 2, 2, 1, 5],
    'B' : [5, 6, 6, 8, 9],
    'C' : [1, 2, 2, 1, 6]
}
dfdouble = pd.DataFrame(data_double)

# mengetahui data duplikat
# print(dfdouble.duplicated())
# filter = dfdouble.duplicated()
# print(dfdouble[filter])  # menampilkan data duplikat

# mengatasi data duplikat
# dfdouble.drop_duplicates(inplace=True)  # menghapus data duplikat
# print(dfdouble)

df_biodata = pd.read_csv('sample_data/biodata_error.csv')
# print(df_biodata.describe())
# mengetahui data kosong
# merubah data umur yang tidak valid
filter_umur = (df_biodata['Umur'] < 0) | (df_biodata['Umur'] > 100)
index_umur = df_biodata[filter_umur].index
df_biodata.loc[index_umur, 'Umur'] = 40  # mengisi data umur yang tidak valid dengan rata-rata umur

# rubah data jenis kelamin yang tidak valid
# cek
# print(df_biodata['Jenis Kelamin'].unique())  # menampilkan data jenis kelamin yang unik
filter_jk = df_biodata['Jenis Kelamin'].isin(['Laki-laki', 'Perempuan'])
index_jk = df_biodata[~filter_jk].index
df_biodata.loc[index_jk, 'Jenis Kelamin'] = 'Laki-laki'  # mengisi data jenis kelamin yang tidak valid dengan 'Laki-laki'       

# samakan kata "Laki-laki" dan "Perempuan"
df_biodata['Jenis Kelamin'] = df_biodata['Jenis Kelamin'].str.replace('Laki-laki', 'Laki-laki').str.replace('Perempuan', 'Perempuan')

# pisahkan data menggunakan ,
df_biodata['Email   dan POS'].str.split(',', expand=True)  # memisahkan data email dan pos
df_biodata[['Email', 'POS']] = df_biodata['Email dan POS'].str.split(',', expand=True)  # memisahkan data email dan pos menjadi dua kolom

print(df_biodata)