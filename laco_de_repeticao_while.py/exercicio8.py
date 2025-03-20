import os 

os.system ("clear")

 
def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota (entre 0 e 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")


nota1 = ler_nota()
nota2 = ler_nota()
nota3 = ler_nota()


print(f"As notas recebidas foram: {nota1}, {nota2}, {nota3}")
