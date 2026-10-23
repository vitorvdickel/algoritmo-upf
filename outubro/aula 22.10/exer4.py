'''
4 - Faça um programa que recebe dois valores positivos (maiores que zero).
Depois faça 4 funções para implementar as 4 operações básicas entre
esses dois números
'''
import utils

while True:
    n1 = float(input("Informe o valor de n1:"))

    if (n1 < 1):
        print ("Valor inválido")
        continue

    n2 = float(input("Informe o valor de n2:"))

    if (n2 < 1):
        print ("Valor inválido")
        continue

    result_soma = utils.calcularSoma(n1, n2)
    result_subt = utils.calcularSubt(n1, n2)
    result_mult = utils.calcularMult(n1, n2)
    result_div = utils.calcularDiv(n1, n2)

    print ("O valor da soma é: ",result_soma)
    print ("O valor da subtração é: ",result_subt)
    print ("O valor da multiplicação é: ",result_mult)
    print ("O valor da divisão é: ",result_div)