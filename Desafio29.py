# Escrreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$ 7,00 por
# cada Km acima do limite.

velocidade=float(input('Digite a velocidade: ').strip())
if velocidade > 80:
    print('Velocidade: {:.0f} Km'.format(velocidade))
    print('Velocidade Permitida 80Km, multa de R$ 7,00 por Km excedido')
    print('[MULTADO] Velocidade excedida: {:.0f}Km'.format(velocidade-80))
    print('Valor da multa: R$ {:.2f}'.format((velocidade-80)*7))

