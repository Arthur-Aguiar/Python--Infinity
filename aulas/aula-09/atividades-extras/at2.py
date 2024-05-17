class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def cor(self):
        pass  

    def modelo(self):
        pass  

class Carro(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def cor(self):
        return "azul"

    def modelo(self):
        return "Gol G1"

carrinho = Carro("Gol")

class bike(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def cor(self):
        return "Vermelha"

    def modelo(self):
        return "Cross Country"

bikezinha = bike("Monark")

print("Carro")
print(f"Nome: {carrinho.nome}")  
print(f"Cor: {carrinho.cor()}")  
print(f"Modelo: {carrinho.modelo()}")  
print()
print("Bicicleta")
print(f"Nome do : {bikezinha.nome}")  
print(f"Cor do : {bikezinha.cor()}")  
print(f"Modelo do : {bikezinha.modelo()}")  