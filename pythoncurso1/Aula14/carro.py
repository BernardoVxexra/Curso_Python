class Carro:
   def __init__(self,marca,modelo,cor,combustivel): #utilizado pois diz que vc está se refirindo a ela mesma, 1 sempre self
           self.marca = marca
           self.modelo = modelo
           self.cor = cor
           self.combustivel = combustivel

           self.ligado = False  
           self.velocidade = 0


   def ligar(self):
         if self.ligado:
                  print("Carro já esta ligado")
         else:
                  print(f"{self.modelo} Ligado")
                  self.ligado = True

def desligar(self):
                    
                    if self.ligado:
                     print(f"{self.modelo} desligado")     
                     self.ligado = False
                     print("Carro já esta ligado")
                    else:
                        print("Carro já está ligado")
        
def acelerar(self):
               if self.ligado:
                   self.velocidade += 1
                   print(f"{self.velocidade} km/h")   
               else:
                   print("NÃO É POSSIVEL ACELERAR CARRO DESLIGADO")    
                   
def frear(self):
               if self.ligado:
                   self.velocidade -= 1
                   print(f"{self.velocidade} km/h")   
               else:
                   print("NÃO É POSSIVEL FREAR, CARRO DESLIGADO") 