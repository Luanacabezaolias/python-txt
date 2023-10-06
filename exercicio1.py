'''Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada 
linha).
'''
arquivo = open('numeros.txt','w')

for i in range(10):
    numero = str(input('Insira um número: '))
    arquivo.write(numero + '\n')
arquivo.close()