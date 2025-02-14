import os

os.system ("clear")

primeira_nota= float(input("digite a sua primeira nota: "))
segunda_nota= float(input("digite a sua segunda nota: "))
terceira_nota= float(input("digite a sua  terceira nota:  "))


media=( primeira_nota + segunda_nota + terceira_nota) /3

if media == 7:
    print ("aprovado")
if media > 7:
    print ("aprovado")
else:
    print("reprovado")

    print(media)

    
    

