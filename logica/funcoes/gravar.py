arquivo = open('arqtexto.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#Leitura do arquivo texto
leitura = open('arqtexto.txt', 'r')
print(leitura.read())
leitura.close()