'''Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário 
grave diversos caracteres nesse arquivo até que seja digitado o caractere “0” (zero).'''

with open('arquivo.txt', 'w') as arquivo:

    while True:
        caracter = input('Digite algma coisa (0 para finalizar): ')
        if caracter == '0':
            break
        arquivo.write(f'{caracter}\n')
