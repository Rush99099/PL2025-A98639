class Parser:
    def __init__(self, input_str):
        self.input = input_str.replace(' ', '')  # remove espaços
        self.pos = 0

    def peek(self):
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None

    def consume(self):
        c = self.peek()
        self.pos += 1
        return c

    def parse(self):
        result = self.E()
        if self.peek() is not None:
            raise Exception(f"Erro: caractere inesperado '{self.peek()}' na posição {self.pos}")
        return result

    # E → T E'
    def E(self):
        result = self.T()
        return self.Ep(result)

    # E' → + T E' | - T E' | ε
    def Ep(self, acc):
        c = self.peek()
        if c == '+':
            self.consume()
            acc += self.T()
            return self.Ep(acc)
        elif c == '-':
            self.consume()
            acc -= self.T()
            return self.Ep(acc)
        else:
            return acc  # ε

    # T → F T'
    def T(self):
        result = self.F()
        return self.Tp(result)

    # T' → * F T' | / F T' | ε
    def Tp(self, acc):
        c = self.peek()
        if c == '*':
            self.consume()
            acc *= self.F()
            return self.Tp(acc)
        elif c == '/':
            self.consume()
            divisor = self.F()
            if divisor == 0:
                raise Exception("Erro: divisão por zero")
            acc /= divisor
            return self.Tp(acc)
        else:
            return acc  # ε

    # F → ( E ) | num
    def F(self):
        c = self.peek()
        if c == '(':
            self.consume()
            result = self.E()
            if self.consume() != ')':
                raise Exception("Erro: parêntese fechado esperado")
            return result
        elif c.isdigit():
            return self.number()
        else:
            raise Exception(f"Erro: número ou '(' esperado, mas encontrou '{c}'")

    def number(self):
        num_str = ''
        while self.peek() and self.peek().isdigit():
            num_str += self.consume()
        return int(num_str)


# Exemplo de uso:
if __name__ == "__main__":
    while True:
        expr = input("Digite a expressão (ou 'sair' para terminar): ")
        if expr.lower() == 'sair':
            break
        try:
            parser = Parser(expr)
            result = parser.parse()
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Erro: {e}")
