from tarefas import *
from meu_modulo import *

banco_de_dados = []

while True:
    print("1 - Adicionar nova tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Listar por prioridade")
    print("4 - Listar por categoria")
    print("5 - Marcar tarefa como concluída")
    print("6 - Remover tarefa")
    print("7 - Sair")

    op = int(input("-> "))

    if op == 1:
        adicionar_tarefa()
    elif op == 2:
        listar_tarefa()
    elif op == 3:
        listar_por_prioridade()
    elif op == 4:
        listar_por_categoria()
    elif op == 7:
        break


adicionar = adicionar_tarefa
listar_tarefa = listar_tarefa
listar_prioridades = listar_por_prioridade
listar_categoria = listar_por_categoria
tarefa_concluida = concluir_tarefa
tarefa_remover = remover_tarefa

print(tarefa_remover)