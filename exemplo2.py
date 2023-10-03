nomes = []

#ler o arquivo txt linha por linha
arquivo = open('nomes.txt','r')     # r = read

#percorre o arquivo linha por linha
for linha in arquivo:
    print(linha, end='')
    nomes.append(linha)

print(nomes)


numeros = []

for linha in arquivo:
    numeros.append(int(linha))

print(numeros)
print(f'Somatório: {sum(numeros)}')

arquivo.close()