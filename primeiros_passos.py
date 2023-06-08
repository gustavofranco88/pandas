import pandas as pd
import zipfile

with zipfile.ZipFile('C:\\Users\\Asus\\PycharmProjects\\zipdados.zip', 'r') as zip_dados:
    zip_dados.extractall('C:\\Users\\Asus\\PycharmProjects')

df_origem = pd.read_csv('C:\\Users\\Asus\\PycharmProjects\\origem-dados.csv')
df_tipos = pd.read_csv('C:\\Users\\Asus\\PycharmProjects\\tipos.csv')

print(df_origem.head(50))
print(df_origem.tail(10))
print(df_origem.info)
print(df_origem.describe())

coluna = df_origem
print(coluna)

filtro = df_origem[df_origem['tipo'] > 3]
print(filtro)

ordenados = df_origem.sort_values('status')
print(ordenados)

agrupado = df_origem.groupby('tipo').mean
print(agrupado)
'''
for grupo in agrupado:
    print(grupo) 
'''

import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nome': ['João', 'Maria', 'Ana']})

# DataFrame 2
df2 = pd.DataFrame({'ID': [2, 3, 4],
                    'Idade': [25, 30, 35]})

# Mesclando os DataFrames com base na coluna 'ID'
merged_df = pd.merge(df1, df2, on='ID')

print(merged_df)


df1 = pd.DataFrame({'id': [0, 1, 2],
                     'nome': ['Joao', 'Luan', 'Jean']})

df2 = pd.DataFrame({'id': [1, 2, 3],
                     'idade': [21, 33, 29],
                    'cor': ['azul', 'preto', 'cinza']})

df3 = pd.merge(df1, df2[['id', 'cor']], on='id')
print(df3)
