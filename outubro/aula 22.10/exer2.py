#Uso da função lambda
'''
2 - Faça um programa em Python que solicite ao usuário o preço de
um produto e o percentual de desconto que será aplicado. O programa
deverá utilizar uma função lambda para calcular o valor final do
produto após a aplicação do desconto e apresentar o resultado na tela
'''

preco = float(input("Informe o preço do produto em R$: \n"))
desco = float(input("Informe o desconto do produto em %: \n"))

calcularPreco = lambda p, d: p - (p * d / 100)

precoFinal = calcularPreco(preco,desco)

print("O valor do produto é de R$", preco)
print("O desconto aplicado é foi de", desco,"%")
print(f"O valor final é de R$ {precoFinal:.2f}",)