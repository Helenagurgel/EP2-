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
