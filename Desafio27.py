# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
# Exemplo: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print(nome)
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))