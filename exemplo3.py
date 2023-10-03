#criar arquivo de texto

arquivo = open('escrever.numeros.txt', 'w')    # w = write

arquivo.write('este texto será escrito no programa\n')
arquivo.write('essa outra linha tambem será escrito no programa\n')

nome = input('Digite seu nome: ')
arquivo.write(nome + '\n')

idade = int(input('Digite sua idade: '))
arquivo.write(str(idade) + '\n')

arquivo.close()