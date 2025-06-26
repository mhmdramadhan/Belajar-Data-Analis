# dataset
# file excel, json, csv
# Pandas IO tools
# Membaca Data
import pandas as pd

# membaca file csv
path = 'sample_data/provinsi_indonesia.csv'
df_csv = pd.read_csv(path, sep=',', index_col=0)
# print(df_csv)

# membaca file excel
path = 'sample_data/provinsi_indonesia.xlsx'
df_excel = pd.read_excel(path, sheet_name='provinsi')
# print(df_excel)

# membaca file json
path = 'sample_data/provinsi_indonesia.json'
df_json = pd.read_json(path)
# print(df_json)

# Output 
# Menulis Data
# Menulis file csv
# df_csv.to_csv('sample_data/provinsi_indonesia_output.csv')

# menulis file excel
# df_excel.to_excel('sample_data/provinsi_indonesia_output.xlsx')

# menulis file json
# df_json.to_json('sample_data/provinsi_indonesia_output.json')

# Menyiapkan Data
# Method Head
heads = df_csv.head(10)  # Menampilkan 10 baris pertama
# Method Tail
tails = df_csv.tail(10)  # Menampilkan 10 baris terakhir
# Method Sample
samples = df_csv.sample(10)  # Menampilkan 10 baris acak
# print("Heads:\n", heads)


# pandas options display
pd.options.display.max_rows = None  # Set jumlah baris maksimum yang ditampilkan
# pandas options display width
pd.options.display.width = 3  # Set jumlah kolom maksimum yang ditampilkan

path_pokemon = 'sample_data/Pokemon.csv'
df_pokemon = pd.read_csv(path_pokemon, index_col=0)
# print("Pokemon DataFrame:\n", df_pokemon)

# mencari rata rata data
# display precision
pd.options.display.float_format = '{:.2f}'.format
mean_values = df_pokemon.mean(numeric_only=True)
# print("Rata-rata nilai:\n", mean_values)

# method info dan macam tipe data
info = df_pokemon.info()
# print("Info DataFrame:\n", info)

# method describe dan statistik
# print("Statistik Deskriptif:\n", df_pokemon.describe().transpose())
# print describe include object
# print("Statistik Deskriptif (termasuk objek):\n", df_pokemon.describe(include=['object']).transpose()) 

# semua kolom/baris describe
# mean
# print("Statistik Deskriptif (semua kolom):\n", df_pokemon.mean(numeric_only=True))
# standard deviasi
# print("Standard Deviasi:\n", df_pokemon.std(numeric_only=True))
# min
# print("Nilai Minimum:\n", df_pokemon.min(numeric_only=True))
# kemiringan skewness
# print("Kemiringan (Skewness):\n", df_pokemon.skew(numeric_only=True))
# kolom tertentu
print("Statistik Mean (kolom tertentu):\n", df_pokemon[['HP', 'Attack', 'Defense']].mean())
 
