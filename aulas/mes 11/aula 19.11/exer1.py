'''
Desenvolva um programa em Python que utilize um dicionário para armazenar os 
dados de "n" alunos. Para cada aluno, devem ser registrados nome, idade e 
nota final. O programa deverá:
a) Solicitar os dados dos cinco alunos.
b) Armazenar as informações em um dicionário.
c) Apresentar o nome e a nota de cada aluno.
d) Calcular e apresentar a média das notas.
e) Identificar e apresentar o aluno com a maior nota.
'''

alunos ={}
soma_notas = 0

n = int(input("Informe o número de alunos:"))

for i in range(n):
    print (f'Informe os dados do {i+1}° alunos:')
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    nota = float(input('Informe a nota final: '))
    if (nota > 10 or nota < 0):
        print ('Valor inválido')
        nota = float(input('Informe a nota final: '))

    alunos[i+1] = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    soma_notas += nota

print ("Dados dos alunos:")
for chave, infos in alunos.items():
    print(f'\nAluno {chave}:')
    for campo, valor in infos.items():
        print(campo,':',valor)

# Calcular média
media = soma_notas / n

print ("\nA media das notas é:",media)

# Verificar maior nota
maior_nota = -1
melhor_aluno = ""

for chave, infos in alunos.items():
    if infos["nota"] > maior_nota:
        maior_nota = infos["nota"]
        melhor_aluno = infos["nome"]

print('\nAluno com a maior nota:')
print('Nome:', melhor_aluno)
print('Nota:', maior_nota)