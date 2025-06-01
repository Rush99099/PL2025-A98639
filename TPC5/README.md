# Simulador de Máquina de Vending

Bruno Campos  
A98639  


## Resumo

Este projeto implementa uma máquina de vending em Python, simulando a compra de produtos através de comandos do utilizador.  
O programa carrega um stock inicial a partir do ficheiro `stock.json` e permite:

- listar produtos disponíveis
- inserir moedas (com soma automática do saldo)
- selecionar produtos (verificando saldo e stock)
- devolver troco no final
- adicionar novos produtos ou repor stock

No final, o stock atualizado é gravado de volta no ficheiro `stock.json`, garantindo persistência entre execuções.  
O programa também trata casos de erro, como códigos inexistentes, saldo insuficiente ou stock esgotado.


## Testes e Resultados

Estes são exemplos de uso:
- LISTAR
- MOEDA 1e, 20c, 5c
- SELECIONAR A23
- ADICIONAR D56 chupa 10 0.5
- SAIR

Com o seguinte resultado:

LISTAR
cod | nome | quantidade | preço
---------------------------------
A23 Ã¡gua 0.5L 8 0.7€
B12 coca-cola 5 1.2€
C34 sumo laranja 3 1.0€

MOEDA 1e, 20c, 5c
maq: Saldo = 1.25€

SELECIONAR A23           
maq: Pode retirar o produto dispensado "Ã¡gua 0.5L"
maq: Saldo = 0.55€
ADICIONAR D56 chupa 10 0.5
maq: Produto CHUPA atualizado/adicionado.

SAIR
maq: Pode retirar o troco: 1x 50c, 1x 5c.
maq: Até à próxima