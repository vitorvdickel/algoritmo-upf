'''
2 - Faça um programa em Python que recebe 5 números inteiros em uma lista
apresente:
- a lista em ordem decrescente
- a soma dos numeros desta lista (sem usar a função sum)
- e quantos valores são maiores que 10
'''

listaN = []

for i in range(5):
    valor = int(input("Informe o valor:\n"))
    listaN.append(valor)
print ('Lista:',listaN)

# Lista em forma decresente
listaN.sort(reverse=True)
print('A lista em ordem decrescente é', listaN)

# Soma da lista sem função sum
soma = 0
for i in range (len(listaN)):
    soma = soma + listaN[i]
    result = soma
print ('A soma dos elementos é igual a', result)
    
# Quantos valores são maiores que 10
acum = 0
for i in range (5):
    if listaN[i] > 10:
        acum = acum + 1
print ('Números de elementos maiores que 10:', acum)
