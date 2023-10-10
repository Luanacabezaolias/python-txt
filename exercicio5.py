'''Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo 
arquivo, colocando-os em ordem crescente.'''

lista = []

with open('pares.txt', 'r') as pares:
    for linha in pares:
        lista.append(linha)

with open('impares.txt', 'r') as impares:
    for linha in impares:
        lista.append(linha)

print(linha)
lista.sort()
print(lista)

with open('numeros.txt', 'w') as numeros:
    for num in lista:
        numeros.write(f'{num}\n')