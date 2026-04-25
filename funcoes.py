import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        r = random.randint(1,6)
        lista.append(r)
    return lista

def calcula_pontos_soma(lista):
    soma = 0 
    for i in range(len(lista)):
        soma += lista[i]
    return soma
            

def calcula_pontos_sequencia_baixa(lista):
    
    for i in range(1, 6):
        if i in lista and i+1 in lista and i+2 in lista and i+3 in lista:
            return 15
    return 0


def calcula_pontos_sequencia_alta(lista):
    for i in range(1, 6):
        if i in lista and i+1 in lista and i+2 in lista and i+3 in lista and i + 4 in lista:
            return 30
    return 0






def calcula_pontos_full_house(lista):
    full = 0 
    trio = False
    dupla = False 
    for i in lista:
        verifica = 0 
        for j in range(len(lista)):
            if i == lista[j]:
                verifica += 1
        if verifica == 3:
            trio = True
        elif verifica == 2:
            dupla = True               
        if verifica == 4:
            trio = False
                 
    if trio == True and dupla == True:
        soma = 0 
        for i in range(len(lista)):
            soma += lista[i]
        return soma
    return 0
         

def calcula_pontos_quadra(lista): 
    quadra = 0 
    quarteto = False
    for i in lista:
        verifica = 0 
        for j in range(len(lista)):
            if i == lista[j]:
                verifica += 1
        if verifica >= 4 :
            quarteto = True        
                 
        if quarteto == True:
            soma = 0 
            for i in range(len(lista)):
                soma += lista[i]
            return soma
    return 0

def calcula_pontos_quina(lista):
    quinteto = False
    for i in lista:
        verifica = 0 
        for j in range(len(lista)):
            if i == lista[j]:
                verifica += 1
        if verifica >= 5:
            quinteto = True
    if quinteto == True:
        return 50 
    return 0 
    
def calcula_pontos_regra_avancada(lista):
    dic = {}
    x = calcula_pontos_quina(lista)
    y = calcula_pontos_quadra(lista)
    z = calcula_pontos_full_house(lista)
    w = calcula_pontos_sequencia_alta(lista)
    v = calcula_pontos_sequencia_baixa(lista)
    u = calcula_pontos_soma(lista)
    dic ["cinco_iguais"] = x
    dic["full_house"] = z
    dic["quadra"] = y
    dic["sem_combinacao"] = u
    dic["sequencia_alta"] = w
    dic["sequencia_baixa"] = v
    return dic



