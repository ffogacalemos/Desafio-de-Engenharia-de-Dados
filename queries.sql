-- Query 1: Qual é a receita total gerada apenas por aluguéis com status Concluído?
SELECT SUM(i.valor_unitario * i.quantidade) AS receita_total_concluidos
FROM alugueis a
JOIN itens_aluguel i ON a.id_aluguel = i.id_aluguel
WHERE a.status_pagamento = 'Concluído';

-- Query 2: Quais são as 3 cidades com o maior número de aluguéis realizados?
SELECT c.cidade, COUNT(a.id_aluguel) AS total_alugueis
FROM alugueis a
JOIN clientes c ON a.id_cliente = c.id_cliente
GROUP BY c.cidade
ORDER BY total_alugueis DESC
LIMIT 3;

-- Query 3: Qual foi o brinquedo ou produto mais alugado, em quantidade total, no último mês?
SELECT i.nome_produto, SUM(i.quantidade) AS total_quantidade
FROM alugueis a
JOIN itens_aluguel i ON a.id_aluguel = i.id_aluguel
WHERE CAST(a.data_evento AS TIMESTAMP) >= current_date - INTERVAL '1 month'
GROUP BY i.nome_produto
ORDER BY total_quantidade DESC
LIMIT 1;
