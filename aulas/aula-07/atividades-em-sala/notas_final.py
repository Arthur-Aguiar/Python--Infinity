alunos = []
notas = []

while True:
    aluno_nome = input("digite o nome do aluno (ou 'sair' para encerrar): ")
    if aluno_nome.lower() == "sair":
        break 
    alunos.append(aluno_nome)
    
    nota1 = float(input("digite a primeira nota do aluno: "))
    nota2 = float(input("digite a segunda nota do aluno: "))
    media_aluno = (nota1 + nota2) / 2
    notas.append(media_aluno)

for i in range(len(alunos)):
    print("Nome do aluno:", alunos[i])
    print("Média das notas:", notas[i])
    
    if notas[i] >= 6:
        print("Aprovado.")
    elif notas[i] >= 3.01:
        print("Recuperação.")
    else:
        print("Reprovado.")
    print()
