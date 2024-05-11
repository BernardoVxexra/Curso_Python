#open("caminho","r")

# Mode
# r - leitura
# a - Append (incrementar)
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita


arquivo = open("Aula12/test3.txt","w") 

#print(arquivo.readable())#função para verificar se o arquivo pode ser lido ou não
#print(arquivo.read())
#print(arquivo.readline())#irá ler a primeira linha do arquivo ou seja "python" 
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())

# lista = arquivo.readlines()#vai transformar todas as listas manipulaveis

# print(lista)

# print(lista[3])

#arquivo.write("Python\n") 

#arquivo.write("C++\n")

#arquivo.write("Terraform\n")



#arquivo.close()

import os


# if os.path.exists("Aula12/test2.txt"):

#  os.remove("Aula12/test2.txt")

# else:

#  print("arquivo não existe")

os.rmdir("Aula12/Novapasta")