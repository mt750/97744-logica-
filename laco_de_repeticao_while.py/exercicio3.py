import os 

os.system("clear")

# Função para solicitar e validar a nota
def solicitar_nota():
    while True:
        try:
            nota = float(input("Digite a nota (entre 0 e 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Solicitar as duas notas
nota1 = solicitar_nota()
nota2 = solicitar_nota()

# Calcular a média aritmética
media = (nota1 + nota2) / 2

# Exibir a média
print(f"A média aritmética do aluno é: {media:.2f}")
