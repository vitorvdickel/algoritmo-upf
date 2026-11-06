# Exemplos de listas, com funções prontas da linguagem

lista1 = ['Java', 'Python', 'C', 'C++']
lista2 = [2,4,1,8,4]

print (lista1)
print (lista2)

# Soma dos elementos:
print ('Soma dos elementos', sum(lista2))

# Tamanho da lista:
print ("O elementos/tamanho da lista é", len(lista1))

# Conta o número de elementos igual ao valor designado
print (lista2.count(4))

# Ordenação dos elementos da lista
lista1.sort()
print(lista1)
lista2.sort(reverse = True) # Ordem decrescente
print(lista2)

