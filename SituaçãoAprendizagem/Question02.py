# 2. Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo (para ser positivo a média deve ser acima de 1).

num1 = int(input('Digite um número '))
num2 = int(input('Digite um segundo número '))
num3 = int(input('Digite um terceiro número '))
num4 = int(input('Digite um quarto número '))

media = (num1 + num2 + num3 + num4) / 4

if media >= 1:
    print('Positivo')
else:
    print('Negativo')