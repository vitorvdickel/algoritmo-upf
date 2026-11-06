
#Exemplo simples
def saudacao():
    print ("Olá, mundo!")

saudacao()
saudacao()
saudacao()

#Função mostrar mensagem
def hello (nome, idade, email):
    print ("Olá",nome,"! Você tem", idade , "anos e seu email é",email)

hello ("Vitor", 20, "emailslegails@hotmail.com")

#Função de retorno de valor
def soma (a, b):
    resultado = a + b
    return resultado

x = soma (30, 70)
print ("Soma igual a", x)

#Exemplo de função
def defineAno(v1):
    anoFuturo = 2026 + v1
    return anoFuturo

anos = int(input("Quantos anos avançar?"))
result = defineAno(anos) #variavel para receber o retorno da função
print ("O futuro foi para o ano de", result)