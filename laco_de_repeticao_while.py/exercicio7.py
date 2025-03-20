import os 

os.system ("clear")

login_correto = "mt750"
senha_correta = "matheus3"


max_tentativas = 3

tentativas = 0

while tentativas < max_tentativas:
    
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    
    if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        tentativas += 1
        print(f"Login ou senha incorretos. Você tem {max_tentativas - tentativas} tentativa(s) restante(s).")


if tentativas == max_tentativas:
    print("Número de tentativas excedido. O programa será finalizado.")
