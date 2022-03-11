# Desafio 07
# Crie um programa que leia as duas notas
# de um aluno, cancule e mostre a sua media

n1 = float(input("Digite a primeira note: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

print("Primeira nota: {}".format(n1))
print("Segunda nota: {}".format(n2))
print("Média: {:.1f}".format(media))
