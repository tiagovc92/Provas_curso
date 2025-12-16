pessoa = {}

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["telefone"] = int(input("Digite seu número: "))
pessoa["email"] = input("Digite o e-mail de contato: ")

print(f"Informações de {"nome"} atualizadas")
print("nome: ", pessoa["nome"])
print("telefone: ", pessoa["telefone"])
print("email: ", pessoa["email"])