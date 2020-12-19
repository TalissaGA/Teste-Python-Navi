alunos = {}
i=0
while i < 5:
    aluno = str(input('Digite o nome do aluno: '))
    if not aluno in alunos:
        alunos[aluno] = int(input('Digite a nota do aluno: '))
    i+=1
#print(alunos)

nota_min = 0
aluno_maior_nota = 'a'
for aluno,nota in alunos.items():
    if nota > nota_min:
        nota_min = nota 
        aluno_maior_nota = aluno 

print('Aluno com maior nota: {0} \nRespectiva nota: {1}'.format(aluno_maior_nota, nota_min))    
    
