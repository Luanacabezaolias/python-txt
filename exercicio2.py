'''Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório 
de todos os números contidos no arquivo.'''

arquivo = open('nomes.txt', 'r') 

soma = 0
for linha in arquivo:
    print(linha, end='')
    soma += int(linha)

print(f'Sommatório: {soma}')
arquivo.close()

