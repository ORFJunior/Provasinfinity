quantidades_alunos = int(input("Quantos alunos possuem na sala? "))
soma_idade = 0

for i in range(1,quantidades_alunos+1):
    idade = int(input("Qual a idade do aluno? "))
    while True:
        soma_idade += idade
        break
        

media = soma_idade//quantidades_alunos
print(f"A media de idade da sala é de {media} anos.")