# Somador on/off

Bruno Campos
A98639

## Resumo do funcionamento do programa

O programa tem de somar todas as sequências de dígitos que encontre num texto, e, sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse
comportamento é desligado. Para reativar esse comportamento, o sistema tem de encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas. Assim que encontrar o caráter “=”, o resultado da soma é colocado na saída. Este comportamente repete-se quando o texto acaba.

## Funcionamento do programa

A função `somador_on_off` implementa a lógica descrita acima. Ela lê um texto de entrada e processa-o conforme as regras especificadas, somando sequências de dígitos e controlando o comportamento com as strings "Off" e "On".

Estando com o terminal no mesmo sítio do repositório, podemos usar o comando **python TPC1.py < input.txt** para que o texto utilizado seja o texto presente no ficheiro [input.txt](/TPC1/input.txt).