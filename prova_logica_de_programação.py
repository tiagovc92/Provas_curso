user_certo = "admin"
senha_certa = "1234"
tentativas = 3 

for i in range (tentativas) :
    usuario = str(input("Digite o nome do usuário: "))
    senha = int(input("Digite a sua senha: "))
    
    if usuario == user_certo and senha == senha_certa : 
        print(f"Bem vindo, {user_certo} ")
    else:
        tentativas_restantes = tentativas - (i + 1) 
        if tentativas_restantes > 0:
            print(f"senha ou nome de usuário incorretos. você ainda tem {tentativas_restantes} chances. ")
            
if usuario != user_certo or senha != senha_certa :
    for _ in range (1):
        print("Acesso bloquado. ")
        
    