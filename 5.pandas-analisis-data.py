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
