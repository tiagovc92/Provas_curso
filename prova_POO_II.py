class veiculo:
    def movimentar (self):
        print("O carro está se movimentando !")
        
class carro (veiculo):
    def movimentar(self):
        print("O carro está dirigindo ")
    
class moto (veiculo):
    def movimentar(self):
        print("A está acelerando !")
    
veiculo = veiculo()
carro = carro()
moto = moto()

veiculo.movimentar()
carro.movimentar()
moto.movimentar()
