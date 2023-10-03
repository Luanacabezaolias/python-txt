# ler arquivo de texto 

arquivo = open('nomes.txt','r')     # r - read 


# copia tofo o conteudo do arquivo para uma string 
texto = arquivo.read()

print(texto)

# fechar o arquivo
arquivo.close()