n = int(input("Quantas pessoas há na turma? "))
soma_idades = 0

for _ in range(n):
    idade = int(input("Digite a idade: "))
    soma_idades += idade

media_idade = soma_idades / n

if media_idade <= 25:
    print("A turma é jovem.")
elif media_idade <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")
