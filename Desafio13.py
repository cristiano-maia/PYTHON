# Desafio 13
# Faça um algoritmo que leia o salario de um funcionario
# e mostre seu novo salario com 15% de aumento

salario = float(input("Digite o valor do salário: "))
aumento = salario * 15 / 100
vfinal = salario + aumento

print("Valor do salário: R$ {:.2f}".format(salario))
print("Aumento: 15%")
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Valor do novo salário: R$ {:.2f}".format(vfinal))