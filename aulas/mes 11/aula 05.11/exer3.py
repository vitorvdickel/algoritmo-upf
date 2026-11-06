'''
3 - Faça um programa em Python que recebe 'n' notas. Armazene essas notas
em uma lista e apresente: 
- A lista com as notas
- A média das notas
- A maior nota
'''

listaN = []

n = int(input("Quantas notas você gostaria de adicionar a essa lista?\n"))

for i in range(n):
    valor = float(input(f"Informe a{i + 1}° nota:\n"))
    listaN.append(valor)

    while (valor < 0 or valor > 10):
        print ("Valor de nota inválido, tente novamente")
        valor = float(input(f"Informe a{i + 1}° nota:\n"))

# Lista com as notas
print ("A lista com as notas:", listaN)

# Calcular média
soma = 0
for i in range (len(listaN)):
    soma = soma + listaN[i]
media = soma / n
print ("A média de notas é igual a:", media)

# Valor da maior nota
listaN.sort(reverse=True)
print ("A maior nota é igual a:", listaN[0])
