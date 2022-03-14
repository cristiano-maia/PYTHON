# Crie um programa que converta a temperatura de ºC para ºF

c = float(input("Informe a temperatura em ºc: "))
# formula para conveter ºC para ºF
f = ((9 * c) / 5) + 32
print("A temperatura de {} ºC corresponde a {} ºF ".format(c,f))