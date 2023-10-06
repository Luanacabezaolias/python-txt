# adicionar conteudo em arquivo de texto ja existente 

arquivo = open('nomes.txt', 'a')        # a - append

while True:
    nome = input("D}igite o nome: (digite 0 para finalizar): ")
    if nome == '0':
        break
    arquivo.write(nome + '\n')

arquivo.close()