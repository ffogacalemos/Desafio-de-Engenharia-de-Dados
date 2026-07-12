import os
import pandas as pd
import duckdb as ddb

# caminho absoluto baseado no local deste arquivo
base_dir = os.path.dirname(os.path.dirname(__file__))
data_path_read = os.path.join(base_dir, 'raw_data')
data_path_write = os.path.join(base_dir, 'processed_data')

# lendo os dados
alugueis = pd.read_json(os.path.join(data_path_read, 'alugueis.json'))
clientes = pd.read_csv(os.path.join(data_path_read, 'clientes.csv'))
itens_aluguel = pd.read_csv(os.path.join(data_path_read, 'itens_aluguel.csv'))

# informações sobre os dados
print('alugueis info:')
alugueis.info()
print('clientes info:')
clientes.info()
print('itens_aluguel info:')
itens_aluguel.info()

#mostrando emails unicos antes da padronização
print('emails unicos anetes da paronização:')
print(clientes['email'].unique())

#padronizando emails para letras minusculas
clientes['email'] = clientes['email'].str.lower()

#mostrando emails unicos para confirmar que a padronização funcionou
print('emails unicos:')
print(clientes['email'].unique())

#verificar datas de cadastros
print('datas de cadastro:')
print(clientes['data_cadastro'].unique())

#colocando em formato unico de data YYYY-MM-DD usando regex
clientes['data_cadastro'] = clientes['data_cadastro'].str.replace(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', regex=True)

#checando se a padronização funcionou
print('datas de cadastro padronizadas:')
print(clientes['data_cadastro'].unique())

#verificando entradas incompletas em clientes
print('entradas incompletas em clientes:')
print(clientes[clientes.isnull().any(axis=1)])

#removendo entradas incompletas em clientes
clientes = clientes.dropna()

#verificando se foi removido corretamente
print('entradas incompletas em clientes após remoção:')
print(clientes[clientes.isnull().any(axis=1)])

#checando se existem itens de aluguel com quantidade menor ou igual a zero
print('itens de aluguel com quantidade menor ou igual a zero:')
print(itens_aluguel[itens_aluguel['quantidade'] <= 0])

#removendo itens de aluguel com quantidade menor ou igual a zero
itens_aluguel = itens_aluguel[itens_aluguel['quantidade'] > 0]

print('itens de aluguel com quantidade menor ou igual a zero:')
print(itens_aluguel[itens_aluguel['quantidade'] <= 0])

#checando se existem nomes de produtos ausentes ou nulos
print('itens de aluguel com nome de produto ausente ou nulo:')
print(itens_aluguel[itens_aluguel['nome_produto'].isnull() | (itens_aluguel['nome_produto'] == '')])

#checando entradas com id_produto 205 em itens de aluguel
print('itens de aluguel com id_produto 205:')
print(itens_aluguel[itens_aluguel['id_produto'] == 205])

#como não existe o produto com id 205, nem outro o qual podemos saber o nome
#iremos colocar o nome como produto desconhecido para não atrapalhar a relação entre as tabelas
itens_aluguel.loc[itens_aluguel['id_produto'] == 205, 'nome_produto'] = 'produto desconhecido'

#checando entradas com id_produto 205 em itens de aluguel
print('itens de aluguel com id_produto 205:')   
print(itens_aluguel[itens_aluguel['id_produto'] == 205])

#gerando arquivos limpos em formato .xlsx para processed data
clientes.to_excel(os.path.join(data_path_write, 'clientes_limpas.xlsx'), index=False)
alugueis.to_excel(os.path.join(data_path_write, 'alugueis_limpos.xlsx'), index=False)
itens_aluguel.to_excel(os.path.join(data_path_write, 'itens_aluguel_limpos.xlsx'), index=False)

#fazendo queries com duckdb
#Query 1: Qual é a receita total gerada apenas por aluguéis com status Concluído?

query1 = """
SELECT SUM(i.valor_unitario * i.quantidade) AS receita_total_concluidos
FROM alugueis a
JOIN itens_aluguel i ON a.id_aluguel = i.id_aluguel
WHERE a.status_pagamento = 'Concluído'
"""

#Query 2: Quais são as 3 cidades com o maior número de aluguéis realizados?
query2 = """
SELECT c.cidade, COUNT(a.id_aluguel) AS total_alugueis
FROM alugueis a
JOIN clientes c ON a.id_cliente = c.id_cliente
GROUP BY c.cidade
ORDER BY total_alugueis DESC
LIMIT 3
"""

#Query 3: Qual foi o brinquedo ou produto mais alugado, em quantidade total, no último mês?
query3 = """
SELECT i.nome_produto, SUM(i.quantidade) AS total_quantidade
FROM alugueis a
JOIN itens_aluguel i ON a.id_aluguel = i.id_aluguel
WHERE CAST(a.data_evento AS TIMESTAMP) >= current_date - INTERVAL '1 month'
GROUP BY i.nome_produto
ORDER BY total_quantidade DESC
LIMIT 1
"""

#Executando queries
with ddb.connect() as conn:
    receita_total_concluidos = conn.execute(query1).fetchdf()
    cidades_mais_alugueis = conn.execute(query2).fetchdf()
    brinquedo_mais_alugado = conn.execute(query3).fetchdf()

#Exibindo resultados
print("Receita total gerada apenas por aluguéis com status Concluído:") 
print(receita_total_concluidos)
print("\nAs 3 cidades com o maior número de aluguéis realizados:")
print(cidades_mais_alugueis)
print("\nO brinquedo ou produto mais alugado, em quantidade total, no último mês:")
print(brinquedo_mais_alugado)