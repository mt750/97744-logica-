# 1 - limpando o terminal.
import os
os.system("clear")

# 2 - solicitando dados para o usuario.

quantidade_maca = int(input("quantas macas voce quer comprar?: "))


 # 3 - verificando.
if quantidade_maca < 12:
   preco_maca = 1,30

else:
   preco_maca = 1,00

valor_total = quantidade_maca * preco_maca

# 4 - exibindo resultados.
print()
print(F"valor total da compra R$ {valor_total:2f}")

