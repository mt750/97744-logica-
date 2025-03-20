import os 

os.system ("clear")


login_correto = "matheus33"
senha_correta = "mt750"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    
    if login == login_correto and senha == senha_correta:
        print("Login e senha corretos! Acesso permitido.")
        break  
    else:
        print("Login ou senha incorretos. Tente novamente.")
