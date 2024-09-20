# 2. Escreva um programa que receba o salário de um funcionário(float), e retorne o resultado do novo salário com reajuste de 35%.

salarioFuncionario = float(input('Digite seu salário: '))
valor = salarioFuncionario

reajuste = valor * 0.35

salarioComReajuste = valor + reajuste
print(f'Salário com reajuste: {salarioComReajuste}')