import os

os.system ("clear")

# Algoritmo para solicitar a nota de um aluno
nota = -1  # Inicializa a variável com um valor fora do intervalo permitido

# Loop para garantir que a nota esteja entre 0 e 10
while nota < 0 or nota > 10:
    # Solicita a nota ao usuário
    nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
    
    # Verifica se a nota está fora do intervalo permitido
    if nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.")

# Exibe a nota informada pelo usuário
print(f"A nota informada foi: {nota}")
