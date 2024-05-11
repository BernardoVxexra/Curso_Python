minha_string = "qualquer texto"
               #01234567891111
               #          0123

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.islower())#ou isupper, retornará boolean ou seja true or false
print(minha_string.strip())#remove espaços entre textos
print(minha_string.replace("u", "U"))
print(len(minha_string))
print(minha_string[2:5]) #indices, funciona como os números acima, 0 = q da frase
print(minha_string.index("u")) #Esta função mostra o indice do número então, u = [1] pois comeca em 0

x = "texto" in minha_string

print(x)

#3 aspas ou podemos usar escape, com o caracter de /n ao lado das palavras
minha_string2 = "linha 1 , \n linha 2 , \n linha 3. "
print(minha_string2)