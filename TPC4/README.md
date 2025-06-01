Analisador léxico escrito em python, para uma liguagem de query com a qual se podem escrever frases do género:
# Analisador Léxico para linguagem de query

Bruno Campos  
A98639

## Resumo do funcionamento do programa

Este trabalho consistiu em desenvolver um analisador léxico para uma linguagem de query similar à SPARQL, capaz de interpretar comandos como:

select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000

## Funcionamento do programa

O analisador lê queries, identifica tokens como `select`, `where`, variáveis (`?nome`), URIs (`dbo:MusicalArtist`), literais (`"Chuck Berry"`), pontuação e limites (`LIMIT 1000`).  
Ele valida a estrutura e devolve a lista de tokens reconhecidos, servindo de base para futuras etapas como análise sintática ou execução real.

## Lista de Resultados

KEYWORD: select
VARIABLE: ?nome
VARIABLE: ?desc
KEYWORD: where
LBRACE: {
VARIABLE: ?s
KEYWORD: a
PREFIXED: dbo:MusicalArtist
DOT: .
VARIABLE: ?s
PREFIXED: foaf:name
STRING: "Chuck Berry"@en
DOT: .
VARIABLE: ?w
PREFIXED: dbo:artist
VARIABLE: ?s
DOT: .
VARIABLE: ?w
PREFIXED: foaf:name
VARIABLE: ?nome
DOT: .
VARIABLE: ?w
PREFIXED: dbo:abstract
VARIABLE: ?desc
RBRACE: }
KEYWORD: LIMIT
NUMBER: 1000