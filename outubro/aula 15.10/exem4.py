#Função recursiva

def soma (numero):
    if numero == 0:
        return 0
    else:
        return numero + soma(numero-1)

print(soma(3)) #Saida = 6

#Função recursiva: loop dentro da própria função