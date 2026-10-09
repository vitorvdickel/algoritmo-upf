'''
3 - Faça um programa que calcule em uma função a média de 4 avaliações.
Em outra função apresente se o aluno foi aprovado ou reprovado, ou se está
em exame (Conforme conceitos de notas da UPF)
'''

def media(p1, p2, p3, p4):
    resultado = (p1 + p2 + p3 + p4) / 4
    return resultado

def situacao(resultados):
    if resultados >= 7:
        print("Aprovado por média")
    elif 5 <= resultados < 7:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")


provas = []

for i in range(4):
    numero = float(input("Inserir notas da avaliação\n"))
    provas.append(numero)

x = media (provas[0], provas[1], provas[2], provas[3])
r = x
print ("Sua média ficou:", r)
situacao (r)

