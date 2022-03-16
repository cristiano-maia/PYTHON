# Crie um programa que leia com o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"
cid=str(input('Em qual cidade você nasceu? ')).strip()
#SANTO tem 4 digitos mas a contagem começa do 0
# .upper() elimina o problema caso o usuario digite em minuscula

print(cid[0:5] .upper() == 'SANTO')