# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa
import math
co = float(input("Cumprimento do cateto oposto: "))
ca = float(input("Cumprimento do cateto adjacente: "))
hi = math.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))