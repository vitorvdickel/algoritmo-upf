'''
Faça um Programa em Python que armazena os nomes e idades de 5 pessoas em
uma matriz, e apresente o nome da pessoa mais nova
'''
matriz = [["",0],["",0],["",0],["",0],["",0]]

print ("Cadastro de nomes e idades")
for l in range (len(matriz)):
    for c in range (len(matriz[l])):
        if c == 0:
            matriz[l][c] = str(input('Digite o nome:\n'))
        else:
            matriz[l][c] = int(input('Digite a idade:\n'))

#Assume que a primeira pessoa é a mais nova
menor_idade = matriz[0][1]
mais_novo = matriz[0][0]

for l in range(len(matriz)):
    if matriz[l][1] < menor_idade:
        menor_idade = matriz[l][1]
        mais_novo = matriz[l][0]

print ("A pessoa mais nova é",mais_novo, "com",menor_idade,"anos")