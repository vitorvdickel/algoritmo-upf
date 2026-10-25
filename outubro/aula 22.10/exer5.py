#Exercício envolvendo listas
'''
5- Faça um programa que inicialize 5 valores em uma Lista. Apresente a Soma e média de todos os números da lista
'''

lista = [10, 20, 40, 50, 150]
soma = 0
print(lista)

for i in range(len(lista)):
    soma = soma + lista[i]

print ('A soma dos elementos da lista é igual a:',soma)

media = soma / 5

print ('A media dos elementos da lista é igual a:',media)
