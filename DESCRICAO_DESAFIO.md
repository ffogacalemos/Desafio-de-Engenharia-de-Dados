# Descrição do Desafio

## Contexto
A empresa fictícia Festa & Cia é especializada em locação de brinquedos e kits para festas.
O negócio está crescendo e precisa organizar os dados para analisar melhor sua operação.

Atualmente, os dados são extraídos de sistemas diferentes, em formatos distintos, e apresentam inconsistências que precisam ser tratadas antes da análise.

O objetivo do desafio é construir um pipeline simples de ETL para coletar, limpar, modelar e consultar os dados de clientes, aluguéis e itens alugados.

## Objetivo
Desenvolver uma solução em Python que:

- processe os arquivos fornecidos,
- aplique regras de limpeza,
- gere bases prontas para análise em formato Excel,
- apresente uma modelagem relacional simples em formato *Star Schema*, e
- contenha consultas SQL para responder perguntas de negócio.

## Bases de Dados
Os dados de entrada estão na pasta `raw_data`.

### clientes.csv
| Campo | Descrição |
|---|---|
| id_cliente | Identificador único do cliente |
| nome | Nome do cliente |
| email | E-mail do cliente |
| cidade | Cidade do cliente |
| data_cadastro | Data de cadastro do cliente |

**Inconsistências esperadas:**
- e-mails com maiúsculas e minúsculas misturados,
- datas em formatos diferentes (`DD/MM/YYYY` e `YYYY-MM-DD`),
- registros incompletos.

### alugueis.json
| Campo | Descrição |
|---|---|
| id_aluguel | Identificador único do aluguel |
| id_cliente | Identificador do cliente associado ao aluguel |
| data_evento | Data de realização do evento |
| status_pagamento | Status do pagamento: `Pendente`, `Concluído` ou `Cancelado` |

### itens_aluguel.csv
| Campo | Descrição |
|---|---|
| id_aluguel | Identificador do aluguel |
| id_produto | Identificador do produto alugado |
| nome_produto | Nome do brinquedo ou produto alugado |
| quantidade | Quantidade alugada |
| valor_unitario | Valor unitário do item |

**Inconsistências esperadas:**
- valores nulos em `nome_produto`,
- quantidades menores ou iguais a zero.

## Tarefas
### Parte 1: Coleta, Limpeza e Qualidade de Dados
Criar um script Python para:

1. Ler os arquivos `clientes.csv`, `alugueis.json` e `itens_aluguel.csv`.
2. Padronizar os e-mails dos clientes para letras minúsculas.
3. Converter as datas de cadastro para o formato `YYYY-MM-DD`.
4. Remover registros incompletos de clientes.
5. Remover itens de aluguel com quantidade menor ou igual a zero.
6. Tratar nomes de produto ausentes.
7. Gerar arquivos limpos em formato `.xlsx` na pasta `processed_data`.

### Parte 2: Modelagem de Dados
Propor uma modelagem relacional simples em *Star Schema* para facilitar as análises.
A solução deve descrever as tabelas dimensão e a tabela fato utilizadas.

### Parte 3: Consultas SQL
Criar um arquivo SQL com consultas para responder as seguintes perguntas:

- Qual é a receita total gerada apenas por aluguéis com status `Concluído`?
- Quais são as 3 cidades com o maior número de aluguéis realizados?
- Qual foi o brinquedo ou produto mais alugado, em quantidade total, no último mês?

### Parte 4: Publicação do Projeto
Depois de finalizar a solução, publicar o projeto em um repositório público no GitHub.
O repositório deve conter todos os arquivos necessários para avaliação:

- código-fonte,
- bases de entrada,
- arquivos processados,
- documentação,
- consultas SQL.

O link do repositório público deve ser enviado como parte da entrega final.

## Estrutura do Projeto

```
.
├── raw_data
│   ├── alugueis.json
│   ├── clientes.csv
│   └── itens_aluguel.csv
├── processed_data
├── src
├── DESCRICAO_DESAFIO.md
├── README.md
├── queries.sql
└── requirements.txt
```

## Entregáveis
O projeto deve conter:

1. Script Python com a lógica de extração, limpeza e transformação na pasta `src`.
2. Arquivos limpos em `.xlsx` gerados pelo pipeline na pasta `processed_data`.
3. `README` com explicação das decisões, instruções de execução e modelagem.
4. Arquivo `.sql` contendo as consultas da etapa analítica.
5. Link do repositório público no GitHub com a solução completa.
