n_alunos = int(input("Digite o numero de alunos: "))

media_geral_turma = 0

for i in range (n_alunos) :
    
    nome_aluno = str(input("Digite o nome do aluno: "))
    n1 = float(input("Digite a sua primeira nota: "))
    n2 = float(input("Digite a sua segunda nota nota: "))
    n3 = float(input("Digite a sua terceira nota: "))
    
    media = (n1 + n2 + n3) /3
    media_geral_turma += media
    
    if media >= 7:
     print(f"{nome_aluno} está aprovado com {media:.2f}")
    elif media < 7 :
     print(f"{nome_aluno} você está reprovado com {media:.2f} !")
     
media_total = media_geral_turma / n_alunos

print(f"A média geral dos alunos é {media_total:.2f}")
    
    
    