class Calculadora:
    def fazersoma(self, num1, num2):
        pass

class Soma(Calculadora):
    def fazersoma(self, num1, num2):
        return num1 + num2

calculadora = Soma()
print(calculadora.fazersoma(1,3))
