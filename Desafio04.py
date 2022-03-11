# Crie um programa que leia algo digitado
# e exibir o maximo possivel do seu tipo de dados

n=input ('digite algo:')

print(type(n))
print('O valor: ',n, ', é do tipo numero? ',n.isnumeric())
print('O valor: ',n, ', é do tipo letras? ',n.isalpha())
print('O valor: ',n, ', é do tipo letras e numeros? ',n.isalnum())
print('O valor: ',n, ', é do tipo letras maiusculas? ',n.isupper())