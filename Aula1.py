def pot_recursiva(b: float, e: int):
    if e == 0:
        return 1
    elif e == 1:
        return b
    else:
        return b * pot_recursiva(b, e-1)

def pot_iterativa(b: float, e: int):
    res = 1
    for i in range(e):
        res *= b
    return res

print(pot_recursiva(2,5))
print(pot_iterativa(2,5))

b = input("Base: ")
einf = input("EInf: ")
esup = input("ESup: ")

for e in range(int(einf), int(esup) + 1):
    print(pot_recursiva(int(b),e))

#################################################################################################

def maior(lista):
    lista.sort()
    return lista[-1]

print(maior([4,2,5,1,3]))
print(max([4,2,5,1,3]))

#################################################################################################

def unzip(l):
    u1 = []
    u2 = []
    for a,b in l:
        u1.append(a)
        u2.append(b)
    return (u1,u2)

lista = [(1, "banana"), (2, "maçã"), (3, "melancia"), (4, "cereja")]

(unzipped1, unzipped2) = unzip(lista)
print(unzipped1)
print(unzipped2)

#################################################################################################

n = int(input("Número: "))
d = {}
for i in range(0,n+1):
    d[i] = i**2
print(d)

#################################################################################################