#adiciona itens à um arquivo

#abrindo para leitura
arquivo = open('escrever.numeros.txt','r')
for linha in arquivo:
    print(linha, end='\n')

arquivo.close()

#abrindo para adicionar nomes
arquivo = open('escrever.numeros.txt','a')      # a = append

while True:
    nome = input('Digite um nome (Diigte 0 caso deseje finalizar o programa)')
    if nome == 0:
        break
    arquivo.write(nome + '\n')

arquivo.close()

