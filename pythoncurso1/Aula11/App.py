try:

    numero = int(input("Digite um número:"))
    print(numero)


    10/0
except ZeroDivisionError:
    print("Divisão por 0 não é possível")
except ValueError:
    print("Digite um número inteiro válido")
except:
    print("Erro inesperado")
finally:
    print("finalizando programa....")
