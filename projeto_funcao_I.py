from tarefas import *
import streamlit as st


st.title("Gerenciador de Tarefas")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Adicionar tarefa",
        "Listar tarefas",
        "Listar por prioridade",
        "Listar por categoria",
        "Concluir tarefa",
        "Remover tarefa"
    ]
)

if menu == "Adicionar tarefa":
    nome = st.text_input("Nome")
    descricao = st.text_area("Descrição")
    prioridade = st.selectbox("Prioridade", [1, 2, 3, 4, 5])
    categoria = st.text_input("Categoria")

    if st.button("Adicionar tarefa"):
        adicionar_tarefa()
        st.success("Tarefa adicionada com sucesso!")

elif menu == "Listar tarefa":
    tarefas = listar_tarefa()
    for t in tarefas:
        st.write(t)

elif menu == "Listar por prioridade":
    p = st.selectbox("Prioridade", [1, 2, 3, 4, 5])
    for t in listar_por_prioridade(p):
        st.write(t)

elif menu == "Listar por categoria":
    c = st.text_input("Categoria")
    if c:
        for t in listar_por_categoria(c):
            st.write(t)

elif menu == "Concluir tarefa":
    nome = st.text_input("Nome da tarefa")
    if st.button("Concluir"):
        if concluir_tarefa(nome):
            st.success("Tarefa concluída!")
        else:
            st.error("Tarefa não encontrada")

elif menu == "Remover tarefa":
    nome = st.text_input("Nome da tarefa")
    if st.button("Remover"):
        if remover_tarefa(nome):
            st.success("Tarefa removida!")
        else:
            st.error("Tarefa não encontrada")