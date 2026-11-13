'''
5 - Faça um programa em Python que recebe em uma lista 'n' número interiros.
Depois faça a ordenação destes valores pelo método bubble sort e apresente
a lista ordenada
'''

listaN = []
n = int(input('Informe o Nº Elementos '))
for i in range(n):
    v = int(input('Valor => '))
    listaN.append(v)

aux = 0

ordenacao = True
while(ordenacao):
    ordenacao = False
    for i in range(n-1):
        if listaN[i] > listaN[i+1]: #se verdade inicia a troca de posições
            aux = listaN[i]
            listaN[i] = listaN[i+1]
            listaN[i+1] = aux
            ordenacao = True
print(listaN)