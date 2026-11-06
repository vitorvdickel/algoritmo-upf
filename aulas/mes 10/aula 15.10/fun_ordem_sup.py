#Função de ordem superior

def calcular (a, b, operacao):
    return operacao(a, b)

soma = lambda x, y: x + y
multiplicacao = lambda x, y: x * y

print (calcular(5, 3, soma))
print (calcular(5, 3, multiplicacao))