'''
Faça um programa em Python que recebe uma matriz 4x3 e apresente quantos
valores são iguais a zero
'''
matriz = [0,0,0],[0,0,0],[0,0,0],[0,0,0]

print ("Informe os dados da Matriz 4x3")
cont = 0

for l in range (len(matriz)):
    for c in range (len(matriz[l])):
        matriz[l][c] = int(input('Matriz ['+ str(l) + ',' + str(c) + ']:'))
        if matriz[l][c] == 0:
            cont += 1


for l in range (len(matriz)):
    for c in range (len(matriz[l])):
        print('|', end = '\t')
        print(matriz[l][c], end='\t')
    print()

print ('Quantidade de valores iguais a zero =', cont)