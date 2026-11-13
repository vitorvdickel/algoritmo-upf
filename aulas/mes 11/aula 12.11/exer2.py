'''
Faça um Programa em Python que recebe duas matrizes A e B 2x2 de valores inteiros e
imprima a matriz C que é a soma das matrizes A e B.
'''
matriz_a = [0,0],[0,0]
matriz_b = [0,0],[0,0]
matriz_c = [0,0],[0,0]

print ("Informe os dados da Matriz A")

for l in range (len(matriz_a)):
    for c in range (len(matriz_a[l])):
        matriz_a[l][c] = int(input('Matriz ['+ str(l) + ',' + str(c) + ']:'))

print ("Informe os dados da Matriz B")

for l in range (len(matriz_b)):
    for c in range (len(matriz_b[l])):
        matriz_b[l][c] = int(input('Matriz ['+ str(l) + ',' + str(c) + ']:'))
        matriz_c[l][c] = matriz_a[l][c] + matriz_b[l][c]

for l in range (len(matriz_c)):
    for c in range (len(matriz_c[l])):
        print('|', end = '\t')
        print(matriz_c[l][c], end='\t')
    print()