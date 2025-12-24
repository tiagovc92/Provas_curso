class conta_bancaria:
    def __init__(self, saldo, titular ):
        self.titular = titular
        self.saldo = saldo
    def depositar (self, valor ):
        if  valor > 0:
            self.saldo += valor 
            print(f"deposito de {valor} foi realizado com sucesso !")
        else :
            print("Valor de depósito inválido ! ")
    def sacar (self,valor):
        if valor > 0 and valor <= self.valor:
            self.saldo -= valor
            print(f" O saque de valor {valor} foi sacado com sucesso !")
        else :
            print("saldo insuficiente ou valor inválido ")
    def exibir_saldo (self):
        print(f" titular: {self._titular}.")
        print(f" Saldo atual: {self._saldo}")
        
        
conta = conta_bancaria("Tago", 10000)

conta.exibir_saldo
conta.deposirtar(500)
conta.sacar(450)
conta.exibir_saldo   
