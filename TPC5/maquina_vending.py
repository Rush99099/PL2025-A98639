import json
import os

# Carregar stock
STOCK_FILE = 'stock.json'

def load_stock():
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_stock(stock):
    with open(STOCK_FILE, 'w') as f:
        json.dump(stock, f, indent=4)

# Mostrar stock
def listar(stock):
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for p in stock:
        print(f"{p['cod']} {p['nome']} {p['quant']} {p['preco']}€")

# Calcular troco em moedas
def calcular_troco(valor):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    centavos = int(round(valor * 100))
    troco = {}
    for m in moedas:
        qtd, centavos = divmod(centavos, m)
        if qtd > 0:
            troco[m] = qtd
    return troco

# Mostrar troco
def mostrar_troco(troco):
    parts = []
    for m, qtd in troco.items():
        if m >= 100:
            parts.append(f"{qtd}x {m//100}e")
        else:
            parts.append(f"{qtd}x {m}c")
    return ', '.join(parts)

# Programa principal
def main():
    saldo = 0.0
    stock = load_stock()
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip().upper()

        if comando == "LISTAR":
            listar(stock)

        elif comando.startswith("MOEDA"):
            partes = comando[6:].split(',')
            for parte in partes:
                parte = parte.strip()
                if parte.endswith('E'):
                    saldo += int(parte[:-1])
                elif parte.endswith('C'):
                    saldo += int(parte[:-1]) / 100
            print(f"maq: Saldo = {saldo:.2f}€")

        elif comando.startswith("SELECIONAR"):
            cod = comando.split()[1]
            produto = next((p for p in stock if p['cod'] == cod), None)
            if not produto:
                print("maq: Produto inexistente")
                continue
            if produto['quant'] <= 0:
                print("maq: Produto esgotado")
                continue
            if saldo < produto['preco']:
                falta = produto['preco'] - saldo
                print("maq: Saldo insuficiente para satisfazer o seu pedido")
                print(f"maq: Saldo = {saldo:.2f}€; Pedido = {produto['preco']:.2f}€")
                continue
            produto['quant'] -= 1
            saldo -= produto['preco']
            print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
            print(f"maq: Saldo = {saldo:.2f}€")

        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            print(f"maq: Pode retirar o troco: {mostrar_troco(troco)}.")
            print("maq: Até à próxima")
            break

        elif comando.startswith("ADICIONAR"):
            parts = comando.split()
            if len(parts) < 5:
                print("maq: Uso: ADICIONAR <cod> <nome> <quantidade> <preço>")
                continue
            cod, nome, quant, preco = parts[1], parts[2], int(parts[3]), float(parts[4])
            produto = next((p for p in stock if p['cod'] == cod), None)
            if produto:
                produto['quant'] += quant
                produto['preco'] = preco
            else:
                stock.append({'cod': cod, 'nome': nome, 'quant': quant, 'preco': preco})
            print(f"maq: Produto {nome} atualizado/adicionado.")

        else:
            print("maq: Comando não reconhecido. Use LISTAR, MOEDA, SELECIONAR, SAIR, ADICIONAR.")

    save_stock(stock)

if __name__ == "__main__":
    main()
