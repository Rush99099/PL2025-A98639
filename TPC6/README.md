# Parser Recursivo Descendente LL(1) para Expressões Aritméticas

Bruno Campos  
A98639

## Resumo do funcionamento do programa

Este programa implementa um **parser LL(1) recursivo descendente** para reconhecer expressões aritméticas simples, calculando diretamente o seu valor.

Ele suporta operações de soma (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`) e também expressões agrupadas entre parênteses.  
A prioridade dos operadores é respeitada corretamente, ou seja, multiplicação/divisão têm prioridade sobre soma/subtração, e parênteses alteram a ordem normal de avaliação.

## Funcionamento do programa

O programa funciona em duas fases principais:
1. **Tokenização:** transforma a string da expressão (ex.: `"2 + 3 * (4 - 1)"`) numa lista de tokens (`['2', '+', '3', '*', '(', '4', '-', '1', ')']`).
   
2. **Parsing e cálculo:** utiliza funções recursivas que refletem a gramática da expressão:
   - `E()` → expressão
   - `Ep()` → continuação da expressão
   - `T()` → termo
   - `Tp()` → continuação do termo
   - `F()` → fator (número ou expressão entre parênteses)

Cada uma destas funções analisa e consome os tokens passo a passo, calculando o resultado durante a análise.

Por exemplo, ao processar a expressão `2 + 3 * 4`, o programa primeiro avalia `3 * 4 = 12`, depois soma `2 + 12 = 14`.

## Como executar o programa

Certifica-te que tens Python instalado.  
Corre o script no terminal:
```bash
python LL1.py
