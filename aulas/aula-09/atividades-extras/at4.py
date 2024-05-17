
class Veiculo:

    def acelerar(self):
        pass  

    def frear(self):
        pass  

class Carro(Veiculo):
    def frear(self):
        return "riiiih!"
    
    def acelerar(self):
        return "ruun!"

class Bicicleta(Veiculo):
    def frear(self):
        return "vrun!"
    
    def acelerar(self):
        return "ruun!"

carro = Carro()
print("Carro frear faz:",carro.frear())
print("Carro acelerar faz:",carro.acelerar())
print()
bicicleta = Bicicleta()
print("Bicicleta frear faz:",bicicleta.frear())
print("Bicicleta acelerar faz:",bicicleta.acelerar())
