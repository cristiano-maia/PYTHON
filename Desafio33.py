#Faça um programa que leia três numeros
# e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# verificando quem é o maior
maior=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))
