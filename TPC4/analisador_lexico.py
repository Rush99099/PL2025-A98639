import re

# Definição dos padrões (tokens)
TOKEN_SPECIFICATION = [
    ('KEYWORD',   r'\b(select|where|LIMIT|a)\b'),
    ('VARIABLE',  r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
    ('PREFIXED',  r'[a-zA-Z]+:[a-zA-Z]+'),
    ('STRING',    r'"[^"]*"(?:@[a-z]+)?'),
    ('NUMBER',    r'\b\d+\b'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('DOT',       r'\.'),
    ('SKIP',      r'[ \t\n]+'),
    ('MISMATCH',  r'.'),
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
get_token = re.compile(tok_regex).match

def lexer(code):
    line_num = 1
    pos = 0
    mo = get_token(code, pos)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            pass  # Ignora espaços em branco e quebras de linha
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Caractere inesperado {value!r} na posição {pos}')
        else:
            print(f'{kind}: {value}')
        pos = mo.end()
        mo = get_token(code, pos)
    if pos != len(code):
        raise RuntimeError('Erro de análise: texto restante não reconhecido.')

if __name__ == '__main__':
    query = '''
    select ?nome ?desc where {
        ?s a dbo:MusicalArtist.
        ?s foaf:name "Chuck Berry"@en .
        ?w dbo:artist ?s.
        ?w foaf:name ?nome.
        ?w dbo:abstract ?desc
    } LIMIT 1000
    '''
    lexer(query)
