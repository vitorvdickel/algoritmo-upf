#Vítor Vieira Dickel
#Matricula: 194935

print ("METAS")

valor_meta = float(input("Digite o valor da sua meta: \n"))
valor_acumulado = 0
total_deposito = 0

while (valor_meta >= valor_acumulado):
    
    total_deposito += 1
    
    print ("Você tem acumulado: R$", valor_acumulado)
    deposito = float(input("Informe o valor do depósito: "))
    print ("Deposito realizado")
    
    valor_acumulado = valor_acumulado + deposito
    
    if (valor_acumulado < valor_meta):
        qnto_falta = valor_meta - valor_acumulado
        print ("Ainda faltam R$", qnto_falta,"para atingir a meta")
    else:
        valor_acima = valor_acumulado - valor_meta
        
        print ("=== META ATINGIDA ===")
        print ("Meta R$", valor_meta)
        print ("Total acumulado R$", valor_acumulado)
        print ("Depósitos realizados: ", total_deposito)
        print ("Valor acima da meta: R$", valor_acima)
        break