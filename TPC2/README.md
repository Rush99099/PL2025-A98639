# Análise de um dataset de obras musicais

Bruno Campos  
A98639

## Resumo do funcionamento do programa

Este programa lê um dataset de obras musicais a partir de um arquivo CSV, processa os dados e gera os resultados seguintes:
- Uma lista ordenada alfabeticamente dos compositores musicais.
- A distribuição das obras por período, indicando quantas obras estão catalogadas em cada período.
- Um dicionário onde cada período está associado a uma lista alfabética dos títulos das obras desse período.

## Funcionamento do programa

A função `dataset_musica` implementa a lógica descrita acima. O programa lê o arquivo [obras.csv](/TPC2/obras.csv) e processa os dados conforme a sua estrutura. Para extrair as informações usei expressões regulares (ER) para separar as colunas de cada linha e atribuindo as variáveis correspondentes. Por fim ordena-se todas as estruturas pelo pedido e imprime-se o resultado.

Para executar o programa, basta chamar a função `dataset_musica()`.