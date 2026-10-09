#Vítor Vieira Dickel
#Matricula: 194935

print ("VERIFICAÇÃO DE CONSUMO DE ENERGIA")
consumo = int(input("Informe o consumo mensal de kWh: \n"))

if (-1 < consumo <= 100):
    print ("Classificação: Consumo Baixo")
elif (100 < consumo <= 200):
    print ("Classificação: Consumo Moderado")
elif (200 < consumo <= 300):
    print ("Classificação: Alto")
    
    if (-1 < consumo > 220):
        print ("Atenção: recomenda-se reduzir o consumo de energia")
    else:
        print ("Tudo nos conformes ;)")
    
elif (consumo > 300):
    print ("Classificação: Muito Alto")
    
    if (-1 < consumo > 220):
        print ("Atenção: recomenda-se reduzir o consumo de energia")
    else:
        print ("Tudo nos conformes ;)")
else:
    print ("Valor inválido")