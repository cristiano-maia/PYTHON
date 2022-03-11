# Desafio 12
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

preco = float(input("Digite o valor do produto: "))
desconto = preco*5/100
vfinal = preco - desconto

print("Valor do produto: R$ {:.2f}".format(preco))
print("Desconto: 5%")
print("Valor do desconto: R$ {:.2f}".format(desconto))
print("Valor a pagar: R$ {:.2f}".format(vfinal))