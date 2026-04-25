import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        r = random.randint(1,6)
        lista.append(r)
    return lista




def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    lista_grande = []
    dados_rolados_novo = []
    # for dado_para_guardar in range(len(dados_rolados)):
    if dado_para_guardar in range(len(dados_rolados)):
        dados_no_estoque.append(dados_rolados[dado_para_guardar])

    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            dados_rolados_novo.append(dados_rolados[i])

    lista_grande =  [dados_rolados_novo, dados_no_estoque]
    return lista_grande





def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    lista_grande = []
    dados_no_estoque_novo = []
    if dado_para_remover in range(len(dados_no_estoque)):
        dados_rolados.append(dados_no_estoque[dado_para_remover])

    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            dados_no_estoque_novo.append(dados_no_estoque[i])
        
        lista_grande = [dados_rolados, dados_no_estoque_novo]
    return lista_grande



def calcula_pontos_regra_simples(lista):
    dic_pontos = {}
    for i in range(1, 7):
        soma = 0 
        for j in lista:
            if j == i:
                soma += j
        dic_pontos[i] = soma
return dic_pontos


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




def calcula_pontos_full_house(






    lista_grande =  [dados_rolados_novo, dados_no_estoque]
    return lista_grande
