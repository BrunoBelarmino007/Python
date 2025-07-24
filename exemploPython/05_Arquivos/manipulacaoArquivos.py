arquivo = open('arqText.txt', 'w')

arquivo.write('Como foi a aula?\n')
arquivo.write('Aula Prática foi OTIMA\n')
arquivo.close()

#Leitura do arquivo de texto
leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()