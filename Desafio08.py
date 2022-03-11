# Desafio 08
# Escreva um programa que leia um valor em metros
# e o exiba convertifdo em centimentos e milimetros

mt = float(input("Digite a quantidade de metros: "))

cm = mt * 100
mm = mt * 1000

print("Metros digitados: {}".format(mt))
print("Corresponte a: {:.0f} centimentos".format(cm))
print("Corresponde a: {:.0f} milimetros".format(mm))
