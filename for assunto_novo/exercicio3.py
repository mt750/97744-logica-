import os

os.system("clear")

import time


numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de multiplicação do número {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
