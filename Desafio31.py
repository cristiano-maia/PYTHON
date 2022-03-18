# Desenvolva um programa que pergunte a distancia
# de uma viagem em KM. Calcule o preço da passagem
# cobrando R$ 0,50 por KM para viagens até 200Km e
# R$ 0,45 para viagens mais longas

d = float(input('Digite a distancia em Km: '))
if d <= 200:
    print('Distancia: {:.0f}Km'.format(d))
    print('Valor por Km é de R$ 0,50')
    print('Valor da passagem: {:.2f}'.format(d*.50))
else:
    print('Distancia: {:.0f}Km'.format(d))
    print('Valor por Km é de R$ 0,45')
    print('Valor da passagem: {:.2f}'.format(d * .45))