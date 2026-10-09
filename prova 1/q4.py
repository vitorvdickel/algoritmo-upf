#Vítor Vieira Dickel
#Matricula: 194935

import random

print ("Jogo de dados")

opcoes = 0
numeros_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pontos_jogador = 0
pontos_pc = 0
empates = 0

while (opcoes != 3):
    print("\nEscolha uma opção: ")
    print ("1 - Jogar rodada")
    print ("2 - Consultar placar")
    print ("3 - Encerrar jogo")
    
    opcoes = int(input("Digite a opção desejada:\n"))

    #Jogar rodada
    if (opcoes == 1):
        dado_jogador = random.choice(numeros_dados)
        dado_pc = random.choice(numeros_dados)
        
        print ("Jogador tirou: ", dado_jogador)
        print ("Computador tirou: ", dado_pc)
        
        if (dado_jogador > dado_pc):
            pontos_jogador += 1
            print ("O jogador venceu a rodada!")
        elif (dado_pc > dado_jogador):
            pontos_pc += 1
            print ("O computador venceu a rodada!")
        else:
            empates += 1
            print ("Ambos tiraram o mesmo valor no dado e não pontuaram nessa rodada")
    
    #Consulta de placar
    elif (opcoes == 2):
        print ("O placar se encontra da seguinte forma")
        print ("O jogador tem ", pontos_jogador, " pontos")
        print ("O PC tem ", pontos_pc, " pontos")
        print ("Houveram ", empates, " até o momento")
        
    #Encerrar jogo
    elif (opcoes == 3):
        print ("====== RESULTADO FINAL =======")
        print ("Jogador: ", pontos_jogador)
        print ("Computador: ", pontos_pc)
        print ("Empates: ", empates)
        
        if (pontos_jogador > pontos_pc):
            print ("O jogador ganhou o jogo!")
        elif (pontos_pc > pontos_jogador):
            print ("O computador ganhou o jogo!")
        elif (pontos_pc == pontos_jogador):
            print ("A partida terminou empatada!")
        else:
            print ("Código quebrou")
    #(esqueci isso na prova)
    else:
        print ("Opção inválida, tente novamente!")
        continue