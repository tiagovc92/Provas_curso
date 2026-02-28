import utils
import streamlit as st

st.set_page_config(page_title="Sistema de hotel", layout="centered")

if "sistema" not in st.session_state:
    st.session_state.sistema = utils.GerenciadorDeReservas()

# ------------------ TÍTULO ------------------
st.title("Sistema de reservas de hotel")
st.divider()

# ------------------ MENU LATERAL ------------------
opcao = st.sidebar.selectbox(
    "Menu",
    [
        "Início",
        "Cadastrar cliente",
        "Listar clientes",
        "Fazer reserva",
        "Ver reservas"
    ]
)

# ------------------ TELAS ------------------

# INÍCIO
if opcao == "Início":
    st.header("Bem-vindo ao sistema!")
    st.write("Use o menu lateral para navegar pelas funcionalidades.")

# CADASTRAR CLIENTE
elif opcao == "Cadastrar cliente":
    st.header("Cadastro de cliente")

    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")

    if st.button("Cadastrar"):
        cliente = st.session_state.sistema.cadastrar_cliente(nome, telefone, email)
        st.success("Cliente cadastrado com sucesso!")

# LISTAR CLIENTES
elif opcao == "Listar clientes":
    st.header("Clientes cadastrados")
    st.info("Aqui aparecerão os clientes cadastrados.")

    clientes = st.session_state.sistema.todos_os_clientes

    if not clientes:
        st.warning("Não há clientes registrados!")
    else:
        for cliente in clientes:
            st.write(f"Nome: {cliente.nome} | E-mail: {cliente.email} | Telefone: {cliente.telefone}")

# FAZER RESERVA
elif opcao == "Fazer reserva":
    st.header("Nova reserva")

    sistema = st.session_state.sistema
    if not sistema.todos_os_clientes:
        st.warning("Não há clientes cadastrados")
    else:
        clientes_id = [i.id for i in sistema.todos_os_clientes]
        numeros_quartos = [i.numero for i in sistema.todos_os_quartos if i.disp]

        id_cliente = st.selectbox("Selecionar cliente", clientes_id)
        num_quarto = st.selectbox("Selecionar quarto", numeros_quartos)

    if st.button("Reservar"):
        sistema.fazer_reserva(id_cliente, num_quarto)
        st.success("Reserva efetuada com sucesso!")

# VER RESERVAS
elif opcao == "Ver reservas":
    st.header("Reservas realizadas")
    st.info("Aqui aparecerão as reservas feitas.")

    sistema = st.session_state.sistema.todos_as_reservas

    if not sistema:
        st.warning("Não há reservas!")
    else:
        for i in sistema:
            st.write(f"Cliente: {i.dono.id} - {i.dono.nome} | Quarto: {i.quarto.numero} - {i.quarto.tipo} | Checkin: {i.checkin} | Checkout: {i.checkout} | Status: {i.status}")
            st.divider()
