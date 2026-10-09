'''
2 - Faça um programa que receba os valores necessários para o cálculo do IMC.
Envie esses valores para uma função e retorne ao programa principal o valor.
Apresente na tela esse valor
'''

def imc (a, p):
    resultado = p / (a*a)
    return resultado


altura = float(input("Digite a sua altura:\n"))
peso = float(input("Digite o seu peso:\n"))

x = imc(altura, peso)
result = x
print ("O seu IMC é: ", result)

if (result < 16):
    print ("Magreza grave")
elif (result < 17):
    print ("Magreza moderada")
elif (result < 18.5):
    print ("Magreza leve")
elif (result < 25):
    print ("Saudável")
elif (result < 30):
    print ("Sobrepeso")
elif (result < 35):
    print ("Vários graus de obesidade")