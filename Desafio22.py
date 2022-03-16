# 22)  Crie um programa que leia o nome completo de uma pessoa
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome

# .strip() elimina os espaços antes e depois do conteudo
# - nome.count(' ') elimina os espaços do conteudo
nome=str(input('Digite seu nome completo: ')).strip()
# nome.upper() converte a str para MAISC.
print('Nome maiusculo: {}'.format(nome.upper()))
# nome.lower() converte a str para MINUSC.
print('Nome maiusculo: {}'.format(nome.lower()))
#len(nome) conta o cumprimento da variavel
print('Cumprimento do nome sem espaço: {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome {} tem {} letras'.format(separa[0], len(separa[0])))