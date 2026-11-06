'''
1 - Criar um programa em Python que cria uma lista original de países
contendo os seguintes elementos: ("Brasil", "Argentina", "Uruguai", Paraguai").
A partir desta lista, executar as seguintes manipulações:
- Exibir a lista atual
- Apresentar quantos elementos tem na lista
- Se foram encontradas na lista ocorrências do termo Paraguai e quantas vezes
- Inserir o país Chile na posição 2 da lista e apesentar novamente a lista
'''

lista1 = ["Brasil", "Argentina", "Uruguai", "Paraguai"]

# Exibir lista
print (lista1)

# Quantos elementos tem na lista
print ("A lista possui", len(lista1),"elementos")

# Ocorrências de Paraguai
print ("Foi encontrado a palavra Paraguai um total de", (lista1).count("Paraguai"), "vezes")

# Adicionar o Chile na segunda posição da lista
lista1.insert (2, "Chile")
print (lista1)