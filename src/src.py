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

 