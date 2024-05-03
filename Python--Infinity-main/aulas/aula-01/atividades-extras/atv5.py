n = int(input("Quantos números você deseja inserir? "))

numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(n)]

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)
