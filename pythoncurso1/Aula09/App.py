#i = 1

#while i < 10:
  # print(i)
 #  i += 1
   
 
#print(i)
#print("terminou")


criancas = ["mae","pai","filho"]

#for item  in  criancas: #este "item" esta representando está lista
   # print(item)


#canal = "Refatorando"

#for letra in canal:
    #print(letra)

#for index in range(len(criancas)):#Range pode receber apenas 3 atributos dentro dele, apenas 1 é obrigatorio
         #aqui está dizendo que ele irá passar como range o tamanho do meu indice, tamanho da lista
 #        print(criancas[index], index)

#for index in range(5):
       # if index == 0:
        #  print("Primeira linha")
       # else:
       #  print(f"Outras linhas {index}")    



#Iniciando Matrizes
matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0], 
]

for linha  in matrix_numeros:
  # print(linha)
    print("-----") 
    for coluna  in linha:
        print(coluna)