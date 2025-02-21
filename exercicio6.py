import os
  
os.system("clear")

# 2 -  solicitando dados para o usuario .
primeiro_numero = int(input("digite o primeiro numero: ")) 
segundo_numero = int(input("digite o segundo numero: "))
terceiro_numero = int(input("digite o terceiro numero: "))

# 3 - verificando o maior e o menor . 
if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
    menor = terceiro_numero


else:
    maior = segundo_numero
    menor = primeiro_numero

# 4 - exibindo resultados
print()
print(f"maior numero: {maior}")
print(F"menor numero: {menor}")
