import os
os.system("clear")

print("""
=============== menu =================
      
codigo      \tprato           \tvalor
          
1             \tpicanha        \t\t25,00
2    \t\tlasanha      \t\t20,00
3     \t\tstrogonoff   \t\t18,00
4      \t\tbife acebolado\t\t15,00
5     \t\tpao com ovo   \t\t15,00
       
""")
opcao = int(input("digite a opcao desejada: "))

match opcao:
    case 1:
      prato = "picanha"
      valor = 25
    case 2:
      prato = "lasanha"
      valor = 20
    case 3:
      prato = "strogonoff"
      valor = 18
    case 4:
      prato = "bife acebolado"
      valor = 15
    case 5:
      prato = "pao com ovo"
      valor = 15

print(f"{opcoes}
