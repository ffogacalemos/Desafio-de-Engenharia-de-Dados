# Projeto Festa & Cia - Pipeline de ETL e Análise de Aluguéis

## Visão Geral
Este projeto implementa um pipeline simples de ETL em Python para a empresa fictícia Festa & Cia.
O objetivo é processar dados de clientes, aluguéis e itens alugados, limpar inconsistências e gerar bases prontas para análise.

## Arquivos Importantes
- `src/src.py`: script Python que realiza a extração, transformação e limpeza dos dados.
- `raw_data/clientes.csv`: dados dos clientes.
- `raw_data/alugueis.json`: dados dos aluguéis.
- `raw_data/itens_aluguel.csv`: itens alugados.
- `processed_data/`: pasta onde os arquivos limpos em `.xlsx` são gerados.
- `queries.sql`: consultas SQL para análise.
- `DESCRICAO_DESAFIO.md`: descrição do desafio e requisitos do projeto.

## Instruções de Execução
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script principal:
   ```bash
   python src/src.py
   ```
3. Verifique os arquivos gerados em `processed_data/`.

## Resultados Esperados
Após a execução, o projeto deverá gerar:
- `processed_data/clientes_limpas.xlsx`
- `processed_data/alugueis_limpos.xlsx`
- `processed_data/itens_aluguel_limpos.xlsx`

## Modelagem de Dados
### Esquema sugerido
A modelagem foi proposta como um *Star Schema* com duas tabelas dimensão e uma tabela fato.

![Diagrama estrela](assets/Diagrama Estrela.png)

### Modelagem em texto
```text
// Tabela Dimensão: Clientes
Table Dim_Clientes {
  id_cliente int [primary key, note: 'Identificador único do cliente']
  nome varchar [note: 'Nome do cliente']
  email varchar [note: 'E-mail do cliente (limpo e em minúsculo)']
  cidade varchar [note: 'Cidade do cliente']
  data_cadastro date [note: 'Data no formato YYYY-MM-DD']
}

// Tabela Dimensão: Produtos
Table Dim_Produtos {
  id_produto int [primary key, note: 'Identificador do produto alugado']
  nome_produto varchar [note: 'Nome do brinquedo ou produto']
}

// Tabela Fato: Aluguéis (A união entre o aluguel e o item)
Table Fato_Alugueis {
  id_aluguel int [note: 'Identificador do aluguel']
  id_cliente int [note: 'Chave estrangeira para o cliente']
  id_produto int [note: 'Chave estrangeira para o produto']
  data_evento date [note: 'Data de realização do evento']
  status_pagamento varchar [note: 'Pendente, Concluído ou Cancelado']
  quantidade int [note: 'Quantidade alugada (maior que zero)']
  valor_unitario decimal [note: 'Valor unitário do item']
}

// Criando os Relacionamentos (As linhas que ligam as tabelas)
// O símbolo ">" indica uma relação de "muitos para um"
Ref: Fato_Alugueis.id_cliente > Dim_Clientes.id_cliente
Ref: Fato_Alugueis.id_produto > Dim_Produtos.id_produto
```

### Tabelas Dimensão
- **Dim_Clientes**
  - id_cliente
  - nome
  - email
  - cidade
  - data_cadastro

- **Dim_Produtos**
  - id_produto
  - nome_produto

### Tabela Fato
- **Fato_Alugueis**
  - id_aluguel
  - id_cliente
  - id_produto
  - data_evento
  - quantidade
  - valor_unitario
  - status_pagamento

## Consultas SQL
As consultas estão no arquivo `queries.sql` e respondem:
- Receita total de aluguéis com status `Concluído`.
- 3 cidades com mais aluguéis.
- Produto mais alugado no último mês.

## Observações
- O projeto usa DuckDB para executar consultas analíticas a partir dos datasets carregados em memória.
- A limpeza inclui padronização de e-mails, conversão de datas e remoção de registros inconsistentes.
