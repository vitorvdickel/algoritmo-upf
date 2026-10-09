#Vítor Vieira Dickel
#Matricula: 194935

print ("=== ACESSO AO LABORATÓRIO ===")

tentativa = 3

while (tentativa != 0):
    tentativa -= 1
    
    acesso = input("Insira o código de acesso: \n")
    senha = input("Insira a senha de acesso \n")
    
    if (acesso != "LAB2026"):
        print ("Usuário ou senha inválido, tente novamente")
        print ("Tentativas restantes", tentativa)
        continue
    else:
        if (senha != "python123"):
            print ("Usuário ou senha inválido, tente novamente")
            print ("Tentativas restantes", tentativa)
            continue
        else:
            print ("Acesso autorizado ao laboratório!")
            break     