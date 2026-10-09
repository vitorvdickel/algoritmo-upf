'''
1 - Faça um programa, com uma função que necessite de um argumento. A função
retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se
seu argumento for zero ou negativo
'''

def verifica_numero (p1):
    result = ""
    if (valor >= 0):
        result = ('P')
    else:
        result = ('N')
    return result

valor = float(input("Insira um valor:\n"))
r = verifica_numero(valor)
print("O valor é ",r)