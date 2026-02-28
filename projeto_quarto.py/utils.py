from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, telefone, email, id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = id

class Quarto:
    def __init__(self, numero, tipo, valor):
        self.numero = numero
        self.tipo = tipo
        self.valor = valor
        self.disp = True

class Reserva:
    def __init__(self, dono, quarto, checkin, checkout):
        self.dono = dono
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Confirmada"

class GerenciadorDeReservas:
    def __init__(self):
        self.todos_os_clientes = []
        self.todos_os_quartos = []
        self.todos_as_reservas = []
        self.gerar_quartos()

    def cadastrar_cliente(self, nome_cliente, telefone_cliente, email_cliente):
        if not self.todos_os_clientes:
            id_novo_cliente = 1
        else: 
            ultimo_cadastrado = self.todos_os_clientes[-1]
            id_novo_cliente = ultimo_cadastrado.id + 1

        novo_cliente = Cliente(nome_cliente, telefone_cliente, email_cliente, id_novo_cliente)
        self.todos_os_clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        if not self.todos_os_clientes:
            print("Nenhum cliente cadastrado!")
        else:
            for cliente in self.todos_os_clientes:
                print(f"Nome: {cliente.nome}")
                print(f"Telefone: {cliente.telefone}")
                print(f"Email: {cliente.email}")
    
    def atualizar_cliente(self, id):
        for cliente in self.todos_os_clientes:
            if cliente.id == id:
                cliente.nome = input("Digite o novo nome: ")
                cliente.email = input("Digite o novo email: ")
                cliente.telefone = input("Digite o novo telefone: ")
                print("Informações atualizadas com sucesso!")
                break
        else:
            print("Cliente não encontrado!")

    def deletar_cliente(self, id):
        for cliente in self.todos_os_clientes:
            if cliente.id == id:
                self.todos_os_clientes.remove(cliente)
                print("Cliente removido com sucesso!")
                break
        else:
            print("Cliente não encontrado!")

    def gerar_quartos(self):
        tipos_quarto = ['Solteiro', 'Casal', 'VIP']
        valores_quartos = { 'Solteiro': 500, 'Casal': 750, 'VIP': 1000}

        for i in range(1, 11):
            tipo = tipos_quarto[i%3]
            valor = valores_quartos[tipo]
            quarto = Quarto(i, tipo, valor)
            self.todos_os_quartos.append(quarto)

    def fazer_reserva(self, id_cliente, num_quarto):
        cliente_encontrado = None
        quarto_encontrado = None

        for cliente in self.todos_os_clientes:
            if id_cliente == cliente.id:
                cliente_encontrado = cliente
                break
        
        for quarto in self.todos_os_quartos:
            if num_quarto == quarto.numero:
                quarto_encontrado = quarto
                break

        if not cliente_encontrado:
            print("O cliente não existe!")
            return
        
        if not quarto_encontrado:
            print("O quarto não existe!")
            return
        
        checkin = datetime.now().replace(hour=15, minute=0, second=0)
        checkout = checkin + timedelta(days=1)

        reserva = Reserva(cliente_encontrado, quarto_encontrado, checkin, checkout)
        self.todos_as_reservas.append(reserva)
        print("Reserva efetuada com sucesso!")
        quarto_encontrado.disp = False

    def listar_reservas(self):
        if not self.todos_as_reservas:
            print("Não há nenhuma reserva.")
            return
        
        for reserva in self.todos_as_reservas:
            print(f"Cliente: {reserva.dono.id} | {reserva.dono.nome}")
            print(f"Quarto: {reserva.quarto.numero}")
            print(f"Checkin: {reserva.checkin}")
            print(f"Checkout: {reserva.checkout}")
            print(f"Status: {reserva.status}")
            print("-"*20)

sistema = GerenciadorDeReservas()

