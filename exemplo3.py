# criar aquivo de texto

arquivo = open('novo arquivo.txt', 'w')     #w - escrita 

arquivo.write('esse texto será escrito no arquivo\n')
arquivo.write('essa outra linha também será escrita no arquivo\n')

nome = input('Digite seu nome: ')
arquivo.write(nome)

idade = int(input('Digite sua idade: '))
arquivo.write(str(idade) + '\n')

arquivo.write(f'Nome: {nome} - Idade:{idade}\n')

arquivo.close()