# 5. Faça um programa que leia um número e imprima seu antecessor e sucessor. 

numero = int(input('Digite um número e eu direi qual é o sucessor e o antecessor dele'))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor do numero {numero} é {antecessor} e o sucessor é {sucessor}')