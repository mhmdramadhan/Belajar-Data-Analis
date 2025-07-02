import pandas as pd

df = pd.read_csv('sample_data/data_perokok.csv', encoding='latin-1', sep=';')

# jumlah data perokok berdasarkan tahun
df_group = df.groupby('Tahun').size()

# jumlah data perokok berdasarkan Umur pada masing masing tahun
df_group_umur = df.groupby(['Tahun', 'Umur']).size()

# jumlah persentasi perokok berdasarkan umur (sudah ada field persentase)
df_group_persen = df.groupby('Umur')['Persentase Perokok'].mean()

print(df_group_persen)  

