#FUNÇÃO EM PYTHON

#def big_mac():
 #    print("sanduiche big mac")

#print("incio")#incio
#big_mac()#execução da função
#print("fim")#fim

def fazer_big_mac(nome):
 print(f"Sanduiche big mac{nome}")

#fazer_big_mac(" Bernardo")
#fazer_big_mac(" leticia")
#fazer_big_mac(" samuel")

def fazer_batata(tamanho):
  print(f"batata {tamanho}")
 
def preparar_refrigerante(tipo,tamanho):
      print(f"{tipo} {tamanho}")

#fazer_big_mac("Bernardo")
#fazer_batata("Grande")
#preparar_refrigerante("Coca","Média")

def fazer_combo_big_mac(nome, tamanho_batata,tipo_refri,tamanho_refri):
   fazer_big_mac(nome)
   fazer_batata(tamanho_batata)
   preparar_refrigerante(tipo_refri,tamanho_refri)

#fazer_combo_big_mac(" Bernardo","Grande","Coca","Média") 

def soma_numeros(num1,num2):
    return num1 + num2

#resultado = soma_numeros(15,20)
#print(resultado)

def maior_numero(lista_num):
   lista_num.sort()
   lista_num.reverse()
   maior_numero = lista_num[0]
   return maior_numero

resultado = maior_numero([1,2,3,4,5,6,7,8,9])
print(resultado)
