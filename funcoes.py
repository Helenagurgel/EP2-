import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        r = random.randint(1,6)
        lista.append(r)
    return lista