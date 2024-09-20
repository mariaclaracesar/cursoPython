# 5. Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista, enumerando-os.

def elementosLista(lista):
    # enumerate é uma função embutida que retorna um iterador que fornece um índice e o valor correspondente em cada iteração. 
    for index, elemento in enumerate(lista, start=1):
        print(f"{index}: {elemento}")

minha_lista = ['maçã', 'banana', 42, True]
elementosLista(minha_lista)