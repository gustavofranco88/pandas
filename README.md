# Gerar um arquivo .sql com pandas!
Crie um script python que:

- descompacte o arquivo dados.zip;
- leia ambos arquivos descompactados (origem-dados.csv e tipos.csv);
Com o arquivo (origem-dados.csv)
- dos dados carregados do arquivo (origem-dados.csv), filtre apenas os dados identificados como "CRÍTICO" na coluna status;
- ordene o resultado filtrado pelo campo created_at;
- inclua um novo campo "nome_tipo" que deverá ser preenchido baseado nos dados carregados do arquivo tipos.csv;
- gere um arquivo (insert-dados.sql) com os inserts (SQL) dos dados gerados nos passos anteriores (considere o nome da tabela como dados_finais e o nome das colunas que constam no arquivo csv);
- com base na estrutura desta tabela, monte uma query que retorne, por dia, a quantidade de itens agrupadas pelo tipo;

IMPORTANTE:
- no diretório onde o script será executado estarão apenas o seu script python e o arquivo zipado;
- o arquivo a ser gerado (insert-dados.sql) deverá ser salvo no mesmo diretório;
