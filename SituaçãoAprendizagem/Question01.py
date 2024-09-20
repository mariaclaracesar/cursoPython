# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista;
# b) maior valor da lista;
# c) menor valor da lista;
# d) soma de todos os elementos da lista;
# e) lista em ordem crescente;
# f) lista em ordem .

L = [5, 7, 2, 9, 4, 1, 3]
print(f'Tamanho da lista {len(L)}')
print(f'Maior valor da lista {max(L)}')
print(f'Menor valor da lista {min(L)}')
print(f'Soma de todos os elementos da lista {sum(L)}')

L.sort
print(f'Lista em ordem crescente {L}')

L.sort(reverse=True)
print(f'Lista em ordem decrescente {L}')






