import os 

os.system ("cls || clear")

# exemplo de uso do laco de repeticao while
idade = int(input("digite sua idade:"))

while idade <18:
    print("nao autorizado. \nsomente maiores de 18.\n")
    idade = int (input("digite sua idade: "))

    print("acesso permitido")
    print("fim")