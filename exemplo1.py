#ler arquivo de texto

#abre o arquivo
arquivo = open('nomes.txt','r')

#copia todo o conteudo do arquivo para uma string
texto = arquivo.read()
print(texto)

#fecha o arquivo
arquivo.close()