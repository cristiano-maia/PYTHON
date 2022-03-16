# Faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos digitos separados
# Exemplo: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
num = int(input('Digite um numero entre 0 a 9999: '))
# convertendo a variavel num para str
n = str(num)
# irá retornar com a casa 4 .format(n[3]) - 0,1,2,3
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

