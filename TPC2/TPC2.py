import re

def dataset_musica():
    with open('obras.csv', 'r', encoding='utf-8') as file:
        data = file.read()

    # Usa expressões regulares para dividir os dados em linhas
    rows = re.split(r'\n(?=\w)', data)

    # Extrai o cabeçalho e remove-o da lista de linhas
    header = rows[0].split(';')
    rows = rows[1:]

    # Inicializar estruturas de dados
    composers = set()
    period_distribution = {}
    period_titles = {}

    # Process each row
    for row in rows:
        # Usa expressões regulares para separar os campos, ignorando os pontos e vírgulas dentro de aspas
        columns = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', row)
        nome = columns[0].strip()
        periodo = columns[3].strip()
        compositor = columns[4].strip()

        # Adicionar compositor à lista
        composers.add(compositor)

        # Adicionar obra ao período
        if periodo not in period_distribution:
            period_distribution[periodo] = 0
        period_distribution[periodo] += 1

        # Adicionar título da obra ao período
        if periodo not in period_titles:
            period_titles[periodo] = []
        period_titles[periodo].append(nome)

    # Ordenar compositores alfabeticamente
    sorted_composers = sorted(composers)

    # Ordenar títulos por período
    for periodo in period_titles:
        period_titles[periodo].sort()

    # Resultados
    print("Lista ordenada alfabeticamente dos compositores musicais:")
    for composer in sorted_composers:
        print(composer)

    print("\nDistribuição das obras por período:")
    for periodo, count in period_distribution.items():
        print(f"{periodo}: {count} obras")

    print("\nDicionário de títulos das obras por período:")
    for periodo, titles in period_titles.items():
        print(f"{periodo}: {titles}")

if __name__ == '__main__':
    dataset_musica()