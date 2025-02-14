import os

os.system ("clear")


primeiro_numero= float(input("digite seu primeiro numero: "))
segundo_numero= float(input("digite seu segundo numero: "))



media= (primeiro_numero + segundo_numero ) / 2
soma=(primeiro_numero + segundo_numero)
produto=(primeiro_numero * segundo_numero)

if  primeiro_numero < segundo_numero:
    maior_numero = segundo_numero
    menor_numero = primeiro_numero
    
    

else:
    maior_numero = primeiro_numero
    menor_numero = segundo_numero





print()
print("sua media e:", media)

print()
print("sua soma e:", soma )

print()
print("seu produto e:", produto)

print()
print("maior numero e:",  maior_numero)

print()
print("menor numero:", menor_numero)





 

 
    