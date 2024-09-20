# 3. Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor.

numeros = []

for _ in range(20):
    valor = int(input('Digite um número '))
    numeros.append(valor) 

media = sum(numeros) / 20
print(f'Média dos números {media}')

maiorValor = max(numeros)
print(f'Maior valor dos números {maiorValor}')

menorValor = min(numeros)
print(f'Menos valor dos números {menorValor}')


