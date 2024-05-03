nome = input("Digite Nome e Sobrenome do aluno: ")

notas = []

for _ in range(2):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota) #Adiciona elemento ao final da lista.


media = (notas[0] + notas[1]) / 2

print("Nome do aluno:", nome)
print("Média das notas:", media)

if media >= 6:
    print("aprovado.")
elif media >= 3.01:
    print("recuperação.")
else:
    print("reprovado.")


    