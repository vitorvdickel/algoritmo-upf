#Primeiro exemplo de matriz (Deus me ajude)

matriz = [[0,0,0],[0,0,0]] #Matriz 2x3, se fosse 3x3 tem que ter mais um colchete de zeros

print ('Informe os dados da Matriz 2x3')

for l in range (len(matriz)):
    for c in range (len(matriz[l])):
        #matriz[l][c] = int(input('Digite um n°: '))
        matriz[l][c] = int(input('Matriz ['+ str(l) + ',' + str(c) + ']:'))

#print(matriz)

for l in range (len(matriz)):
    for c in range (len(matriz[l])):
        print('|', end = '\t')
        print(matriz[l][c], end='\t')
    print()

'''
O end (Segura o braço!): Ele serve para mandar você não descer na parede 
depois de riscar. Em vez de pular para a linha de baixo, o end diz: 
"Continua riscando aí mesmo, na mesma altura, só que pro lado!".

O \t (Dá um pulão!): Ele é o tamanho de um salto grande para a 
direita — tipo a largura de um tacape. Sem ele, um desenho fica esmagado 
em cima do outro. Com o \t, você deixa um espaço bem largo entre cada coisa.
'''