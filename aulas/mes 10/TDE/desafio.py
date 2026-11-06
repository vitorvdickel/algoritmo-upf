#TDE: DESAFIO
'''
Suponha que você trabalhe no suporte de TI de uma escola e um professor, sabendo que você é programador Python,
solicitou um programa para verificar a maior e menor nota de uma turma de 10 alunos
As notas (de 0 a 10) serão digitadas pelo teclado, verificadas e, ao final, os valores da maior para a menor
nota aparecerão na tela do computador
'''

lista = []



for i in range(10):
    notas = float(input(f'Digite a {i + 1}º nota dos alunos: '))

    #validação dos valores das notas
    while notas < 0 or notas > 10:
        print('Valor inválido, tente novamente')
        notas = float(input(f'Digite a {i + 1}º nota dos alunos: '))

    lista.append(notas) #armazena o valor via teclado na lista

print(lista)

#Maior e menor valor
maior = max(lista)
menor = min(lista)

print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')

#Coloca a lista em ordem decrescente de valor
lista.sort(reverse= True)
print(lista)