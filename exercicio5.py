import os

os.system ("clear")  # limpa o terminal . 

  # operacoes logicas 

print ("0la senhor ou senhora,pfv digite sua idade para votar")
print()
sua_idade = int(input("digite sua idade: "))

if sua_idade < 18:
   print("nao pode votar")
elif sua_idade > 65:
   print("nao pode votar")
else:
   print("bom voto") 




