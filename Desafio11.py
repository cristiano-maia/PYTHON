# Desafio 11
# Faça um programa que leia a largura e a altura de
# uma parede em metros, calcule sua area e a quantidade
# de tinta necessario para pinta-la, sabendo que
# cada litro de tinta pinta uma area de 2 m2

altura = float(input("Digite a altura da parede: "))
cumprimento = float(input("Digite o cumprimento da parede: "))

area = altura * cumprimento
tinta = area/2

print("Altura: {:.2}".format(altura))
print("Cumprimento: {:.2}".format(cumprimento))
print("Area: {:.2}".format(area))
print("Litros de tintas: {:.2} lt".format(tinta))