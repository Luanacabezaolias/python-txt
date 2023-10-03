arquivo = open('dados.txt', 'r')

dicionario = {}

for linha in arquivo:
    lista = linha.split(',')
    print(lista)
    dicionario[lista[0]] = [lista[1], int(lista[2]), float(lista[3])]
    
print(dicionario)