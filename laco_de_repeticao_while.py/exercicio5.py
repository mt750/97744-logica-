import os 

os.system ("clear") 
quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("nota invalida, tente novamente.\n")

        else:
            soma += nota
            break

media = soma / quantidade_notas

print(f"media: {media}")
