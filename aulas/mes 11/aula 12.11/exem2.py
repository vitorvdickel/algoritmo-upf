'''
Desenvolver um programa que utiliza um dicionário para armazenar
informações (código, descrição, preço e quantidade) de um produto
'''

#declarando um dicionário de dados
produto ={}

print ('Informaçoes do Produto')
produto["codigo"] = int(input('Informe o código: '))
produto["descricao"] = input('Informe a descricao: ')
produto["preco"] = float(input('Informe o preço: '))
produto["quantidade"] = int(input('Informe a quantidade: '))

print ('\nDados do Produto')
#perconrrendo o dicionario
for chave,valor in produto.items():
    print(chave,':',valor)

print('\nValor total em estoque:',produto["preco"] * produto["quantidade"])