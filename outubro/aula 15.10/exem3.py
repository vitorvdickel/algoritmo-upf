#Uso de switch case em Python

def mostraIdade(i):
    print ("A idade é: ", i)

def mostraNome(n):
    print ("O nome é: ", n)
# ----------------------------------------------------------

print("===== MENU =====")
print("1 - Cadastrar")
print("2 - Consultar")
print("3 - Alterar")
print("4 - Excluir")
print("5 - Sair")

opcao = int(input("Selecione a opção desejada: \n"))

match opcao:
    case 1:
        print ("Opção escolhida - CADASTRAR")
        nome = str(input("Informe o nome\n")).title()
        idade = int(input("Informe a idade\n"))
        mostraIdade(idade)
        mostraNome(nome)
    case 2:
        print ("Opção escolhida - CONSULTAR")
    case 3:
        print ("Opção escolhida - ALTERAR")
    case 4:
        print ("Opção escolhida - EXCLUIR")
    case 5:
        print ("Opção escolhida - SAIR")
    case _:
        print ("Opção inválida")