#Escreva um programa que pergunte o salario de
# um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$ 1.250,00 calcule um
# aumento de 10%. Para salarios igual ou inferior calcular 15%
salario = float(input('Digite o salario: '))
sup = salario*10/100
inf = salario*15/100
if salario > 1250:
    print('Salario atual R$ {:.2f} aumento de R$ {:.2f}'.format(salario, sup))
if salario <= 1250:
    print('Salario atual R$ {:.2f} aumento de R$ {:.2f}'.format(salario, inf))