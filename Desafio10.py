# Desafio 10
# Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos dolares
# ela pode comprar, considerando $ 1,00 a R$ 3,27

carteira = float(input("Digite o valor: "))
dolar = 3.27
compra = carteira/3.27
print("Valor na carteira R$ {:.2f} ".format(carteira))
print("Valor do dolar do dia $ {}".format(dolar))
print("Quantos dolares dá pra comprar? $ {:.2f}".format(compra))