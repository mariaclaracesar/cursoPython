# 6. Crie um programa que converta horas em segundos, conforme o valor que o usuário informar quando solicitado a ele

horas = int(input('Digite a quantidade de horas: '))
horasEmSegundos = horas * 60 * 60
print(f'{horas} horas equivalem a {horasEmSegundos} segundos.')