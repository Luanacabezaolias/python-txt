# ler arquivo de etxto linha pot linha 

arquivo = open('numeros.txt','r')

numeros = []


#percorre o arquivo linha por linha 
for linha in arquivo:
    numeros.append(int(linha))
    
print(numeros)
print(f'Somatório: {sum(numeros)}')
    
    
arquivo.close()
