'''Solicite ao usuário diversos números inteiros (até que seja digitado o número zero). Armazene os 
números pares em um arquivo e os números ímpares em outro arquivo.'''

pares = open('pares.txt','w')
impares = open ('impares.txt','w')

while True:
    numero = int(input("Números: "))
    if numero % 2 == 0:
        pares.write(f'{numero}\n')
    else:
        impares.write(f'{numero}\n')

pares.close()
impares.close()