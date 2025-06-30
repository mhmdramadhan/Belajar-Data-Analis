import pandas as pd


df = pd.read_csv('sample_data/Pokemon.csv')

# filtering data
filter = df['Name'] == 'Pikachu'
# print(df[filter])

# filter berdasarkan hasil dari kolom
filter = df['Attack'] == df['Attack'].max()
# print(df[filter])

# filtering menggunakan query
# query = 'Name == "Pikachu"'
query = 'Attack == Attack.max()'
df_query = df.query(query)
# print(df_query)

# grouping data
# model lama
query = '`Type 1` == "Grass"'
df_group = df.query(query)
# print(df_group.mean(numeric_only=True))
# menggunakan groupby mencari rata-rata
# grupby berdasarkan Type 1
# df_groupby = df.groupby('Type 1').mean(numeric_only=True)
# grupby berdasarkan Type 1 dan Type 2
# df_groupby = df.groupby(['Type 1', 'Type 2']).mean(numeric_only=True)
# print(df_groupby)
# df_groupby.to_excel('sample_data/pokemon_groupby.xlsx')

# group by dengan agg
df_groupby = df.groupby('Type 1').agg({
    'Attack': 'max',
    'Defense': 'min',
    'Speed': 'mean',
    'Total': ['max', 'min']
})
# print(df_groupby)

# membuat fungsi sendiri
def range_func(x):
    return x.max() - x.min()

df_groupby = df.groupby('Type 1').agg({
    'Sp. Atk': range_func,
})
# print(df_groupby)

# Pivot table
# pivot table untuk mencari rata-rata Total berdasarkan Type 1
df_data = df.pivot_table(index = ['Type 1', 'Type 2'], values=['Total', 'Attack', 'Defense'], aggfunc=['mean', 'max', 'min'])
# print(df_data)
# pivot table untuk mencari rata-rata Attack berdasarkan Type 1 dan Stage
df_data = df.pivot_table(index='Type 1', columns='Stage', values='Attack', aggfunc='mean')
# print(df_data)

# Nilai Unique
df = pd.read_csv('sample_data/STEM_Salaries.csv')
# mengetahui jumlah nilai unik pada kolom 'title'
# print(df['title'].nunique())
# mengetahui nilai unik pada kolom 'title'
# print(df['title'].unique())
# mengetahui jumlah nilai berdasarkan kolom 'title'
# print(df['title'].value_counts())

# mengurutkan dataFrame
# print(df.sort_values(by=['title','basesalary'])[['title', 'basesalary', 'company']].head(10))  # Mengurutkan berdasarkan kolom 'basesalary' secara menurun

# mengurutkan berdasarkan kolom yang dipilih
# print(df.set_index('title').sort_index(ascending=False)[['basesalary', 'company']].head(10))  # Mengurutkan berdasarkan kolom 'title' secara menaik

# Menggunakan fungsi pada series dan dataframe
data = {
    'nama' : ['Asep', 'Budi', 'Cici'],
    'gaji_dolar'  : [1000, 2000, 3000],
    'bonus' : [100, 200, 300],
    'pengalaman' : [1, 2, 3]
}
df = pd.DataFrame(data)
def status(gaji):
    if gaji < 1500:
        return 'Junior'
    elif gaji < 2500:
        return 'Middle'
    else:
        return 'Senior'
    
# menambahkan kolom baru dengan fungsi apply
df['status'] = df['gaji_dolar'].apply(status)
def fasilitas(df):
    if df['status'] == 'Senior' and df['pengalaman'] > 2:
        return 'Ada Fasilitas'
    else:
        return 'Tidak Ada Fasilitas'

# menambahkan kolom baru dengan fungsi apply
df['fasilitas'] = df.apply(fasilitas, axis=1)
print(df)    
