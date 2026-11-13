'''
Faça um programa em Python que recebe os valores de uma Matriz 3x3 e o 
valor de K. Escreva uma função para multiplicar os elementos da diagonal 
principal por um  valor k. Sua função deve receber a matriz e k, e retornar 
a matriz resultante.
'''
def chamar_multiplicacao(minha_matriz, multiplicador):
    nova_matriz = []
    
    for l in range(len(minha_matriz)):
        linha = []
        for c in range(len(minha_matriz[l])):
            # Multiplica apenas se estiver na diagonal principal (linha == coluna)
            if l == c:
                linha.append(minha_matriz[l][c] * multiplicador)
            else:
                linha.append(minha_matriz[l][c])
        nova_matriz.append(linha)
        
    return nova_matriz

matriz = [[], [], []]

k = float(input('Insira o valor de K: '))

print("Informe os números da Matriz:")
for l in range(3):
    for c in range(3):
        valor = int(input(f'Matriz [{l},{c}]: '))
        matriz[l].append(valor)

# Chama a função e guarda a matriz retornada na variável 'resultado'
resultado = chamar_multiplicacao(matriz, k)

print("\nMatriz resultante:")
for linha in resultado:
    print(linha)