par = impar = 0

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2:
        impar += 1
    else:
        par += 1

print("Quantidade de números pares:", par)
print("Quantidade de números ímpares:", impar)