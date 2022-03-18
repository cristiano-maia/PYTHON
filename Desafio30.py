#Crie um programa que leia o numero inteiro
# e mostre na tela se ele é par ou impar.


n = int(input('Digite um numero inteiro: '))

if n % 2 == 0:
    print('O numero {} é PAR'.format(n))
else:
    print('O numero {} é IMPAR'.format(n))