#Exercício 3 da última aula - corrigido (adição da média ponderada)

#Função para caluclar a média das notas do aluno
def calcularMedia(a,b,c,d):
    media = (a+b+c+d) / 4
    return media

#Função para verificar a situação acadêmica do aluno
def situacao(resultados):
    if resultados >= 7:
        print("Aprovado por média")
    elif 5 <= resultados < 7:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")

def calcularPeso (n1, n2, n3, n4, p1, p2, p3, p4):
    mediaPonderada = (n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1+p2+p3+p4)
    return mediaPonderada

#Programa principal
while True:

    n1 = float(input("Informa a 1° nota: \n"))
    p1 = int(input("Informe o peso da 1° nota: \n"))

    n2 = float(input("Informa a 2° nota: \n"))
    p2 = int(input("Informe o peso da 2° nota: \n"))

    n3 = float(input("Informa a 3° nota: \n"))
    p3 = int(input("Informe o peso da 3° nota: \n"))

    n4 = float(input("Informa a 4° nota: \n"))
    p4 = int(input("Informe o peso da 4° nota: \n"))

    if (p1 + p2 + p3 + p4 != 10):
        print ("O peso das avaliações não fecham, tente novamente")
        continue
    else:

#Chamando função de calcular média:
        result = calcularMedia(n1,n2,n3,n4)
        print ("A média aritmética é ", result)

#Chamando função para calcular média ponderada:
        mediaPond = calcularPeso(n1,n2,n3,n4,p1,p2,p3,p4)
        print("A média ponderada é:", mediaPond)

#Chamando função para situação do aluno:
        situacao(mediaPond)
        break