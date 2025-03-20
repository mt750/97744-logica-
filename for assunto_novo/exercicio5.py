import os

os.system ("clear")

import time

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    soma += numero

print(f"A soma de todos os números é: {soma}")
