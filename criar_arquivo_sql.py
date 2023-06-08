# importando as lib necessárias
import pandas as pd
import zipfile

# Descompactando arquivo 'dados.zip'
with zipfile.ZipFile('dados.zip', 'r') as zip_dados:
    zip_dados.extractall('C:\\Users\\Asus\\PycharmProjects')

# Criando dataframes com os arquivos cvs descompactados
df_origem = pd.read_csv('C:\\Users\\Asus\\PycharmProjects\\origem-dados.csv')
df_tipos = pd.read_csv('C:\\Users\\Asus\\PycharmProjects\\tipos.csv')

# Filtrando apenas as linhas onde 'status' é = a 'critico'
filtro = df_origem[df_origem['status'] == 'CRITICO']

# Mesclar resultado do filtro com df_tipos
filtro = pd.merge(filtro, df_tipos[['id', 'nome']], left_on='tipo', right_on='id', how='left')

#excluir a coluna 'id' que veio de df_tipos, pois não foi pedida no exercicio
filtro = filtro.drop('id', axis=1)

# Alterar nome da coluna 'nome' para nome_tipo
filtro = filtro.rename(columns={'nome': 'nome_tipo'})

#ordenar pela coluna 'created_at'
filtro = filtro.sort_values('created_at')

# Gerar o arquivo 'insert.sql'
with open('insert-dados.sql', 'w') as insert:
    # ler cada linha do dataframe filtro
    for index, row in filtro.iterrows():
        values = (
            row['created_at'],
            row['product_code'],
            row['customer_code'],
            row['status'],
            row['tipo'],
            row['nome_tipo']
        )
        insert_stmt = "INSERT INTO dados_finais " \
                      "('created_at', 'product_code', 'customer_code', 'status', 'tipo', 'nome_tipo') " \
                      "VALUES ({}, {}, {}, {}, {}, {});\n".format(*values)
        # Escrevendo no arquivo 'insert-dados.sql'
        insert.write(insert_stmt)
print('Arquivo insert-dados.sql, gerado com sucesso!')
