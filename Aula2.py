from re import *

# match retorna tuplo a dizer o que encontrou,
# search retorna tuplo a dizer o que encontrou,
# findall retornam um objeto match,
# sub retorna um texto com as substituições

line1 = "Hello World"

# O ?i: é um modificador que faz com que a pesquisa seja case insensitive.
res1 = match(r'(?i:hello)', line1) #Vai dar match porque a string começa com Hello

res1 = match(r'(hello)', line1) #Não vai dar match porque a string começa com H maiúsculo

res1 = match(r'([Hh][Ee][Ll][Ll][Oo])', line1) #Caso não tivéssemos o modificador ?i: faríamos assim, já que o [ ] representa uma das opções


res = re.findall(r'(</?.*?>)', lineX)

res = re.sub(r'(</?.*?>)', '', lineX)

