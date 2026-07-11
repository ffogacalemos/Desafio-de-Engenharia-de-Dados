import os
import pandas as pd
import numpy as np

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