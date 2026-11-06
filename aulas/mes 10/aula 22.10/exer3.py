#Função de ordem superior: função que aceita outras funções como
#parâmetros ou retornando-as como resultado

'''
3 - Faça um programa em python que solicite ao usuário o preço de um
produto e o percentual de desconto aplicado. O programa deverá utilziar
uma função de ordem superior, que recebe outra função como parâmetro,
para calcular o preço final do produto após a aplicação do desconto
(não utilize a função lambda. As funções deverão ser definidas utilizando
o comando def)
'''
#Função Simples
def calculaPreco(p, d):
    pf = p - (p * d / 100)
    return pf

#Função de ordem superior:
def calculaPreco_final(p, d, operacao):
    return operacao(preco, desco)

#Atribuição de valores
preco = float(input("Informe o preço do produto em R$: \n"))
desco = float(input("Informe o desconto do produto em %: \n"))

#Validação final do código
precoFinal = calculaPreco_final (preco, desco, calculaPreco)
print (f"O valor do preço final ficou R$ {precoFinal:.2f}")