'''
4 - Criar um programa em python que armazene 'n' nomes em uma lista.
Depois pede para o usuário informar um termo de pesquisa. Se o termo
estiver na lista, informe a posição da primeira ocorrência do termo
na lista. Caso contrário informe que o termo não foi encontrado na lista
'''

listaN = []

n = int(input("Quantos nomes gostaria de inserir na lista?\n"))

for i in range(n):
    nomes = str(input(f"Insira o {i + 1}° nome da lista:\n"))
    listaN.append(nomes)
print (listaN)

termo = str(input("Insita o termo de pesquisa:\n"))
aux = 0

for i in range (n):
    if listaN[i] == termo:
        print ("O termo", listaN[i], "aparece na posição", i)
        aux = aux + 1
        break
if aux == 0:
    print ("Termo não encontrado")