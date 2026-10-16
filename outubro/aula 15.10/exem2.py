#Formatação de string

texto = input("Digite um texto: ")

#Funções inbutidas para tratamento de Strings
print("1 - letras Maiúscula: ", texto.upper())
print("2 - letras Minuscula: ", texto.lower())
print("3 - 1° em Maiúsculas: ", texto.capitalize())
print("4 - 1°s em Maiúscula: ", texto.title())
print("5 - Inverte d Mai/Min: ", texto.swapcase())
print("6 - Tamanho da string: ", len(texto))
print("7 - Substitui:         ", texto.replace("Amanhã", "Hoje"))
print("8 - Qttd de letra a:   ", texto.count("a")) #se quiser podemos fazer texto.lower().count("a"))
print("9 - Posição da letra w: ", texto.find("w"))
print("10 - Dividir a string: ", texto.split())
print("11 - Tira Esp. com/fim: ", texto.strip())
print("12 - Verifica início:  ", texto.startswith('Amanhã'))
print("13 - Verifica fim :    ", texto.endswith("dia"))
print("14 - Verifica se é n°: ", texto.isdigit())
palavras = texto.split()
print("15 - Separa com o -:   ","-".join(palavras))