# Faça um programa que leia um angulo qualquer e
# mostre na tela o valor do seno, casseno
# e tangente desse angulo

import math
angulo = float(input("Digite o angulo: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem o COSSENO {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem a TANGENTE {:.2f}".format(angulo, tangente))

