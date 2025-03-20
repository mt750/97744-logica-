import os

os.system ("clear")

import time

numero = int(input("Digite um número: "))


while numero > 0:
    print(numero)
    time.sleep(1)  
    numero -= 1

print("FIM!")