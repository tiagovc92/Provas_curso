banco_de_dados = []

def adicionar_tarefa ():
    nova_tarefa = {
        'nome': input("Digite o nome da tarefa: "),
        'descrição' : input("Digite a descrição: "),
        'prioridade' : int(input("Digite a prioridade (1-5): ")),
        "categoria" : input("Digite a categoria: ")
    }
    banco_de_dados.append(adicionar_tarefa)
    print("tarefa adicionada com sucesso ! da o cu")

print(adicionar_tarefa)
    