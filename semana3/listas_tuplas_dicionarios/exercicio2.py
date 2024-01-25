notas_aluno1 = []
notas_aluno2 = []
notas_aluno3 = []
notas_aluno4 = []

for numero in range (0,4): #a função range cria uma sequencia de numeros inteiros
    nota = int (input ("Digite a nota do aluno 1: "))
    notas_aluno1.append (nota)

for numero in range (0,4): 
    nota = int (input ("Digite a nota do aluno 2: "))
    notas_aluno2.append (nota)

for numero in range (0,4): 
    nota = int (input ("Digite a nota do aluno 3: "))
    notas_aluno3.append (nota)

for numero in range (0,4): 
    nota = int (input ("Digite a nota do aluno 4: "))
    notas_aluno4.append (nota)


medias_alunos = []
media_aluno1 = (notas_aluno1[0]+notas_aluno1[1]+notas_aluno1[2]+notas_aluno1[3])/4
medias_alunos.append(media_aluno1)
media_aluno2 = (notas_aluno2[0]+notas_aluno2[1]+notas_aluno2[2]+notas_aluno2[3])/4
medias_alunos.append(media_aluno2)
media_aluno3 = (notas_aluno3[0]+notas_aluno3[1]+notas_aluno3[2]+notas_aluno3[3])/4
medias_alunos.append(media_aluno3)
media_aluno4 = (notas_aluno4[0]+notas_aluno4[1]+notas_aluno4[2]+notas_aluno4[3])/4
medias_alunos.append(media_aluno4)

num_alunos = 0

for media in medias_alunos: 
        if media >= 7:
            num_alunos += 1

print (f'O número de alunos com média igual ou maior a 7 é {num_alunos} alunos.')
