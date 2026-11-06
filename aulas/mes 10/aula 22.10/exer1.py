#Função Recursiva: Fatorial
def calculaFatorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * calculaFatorial(n - 1))

v = int(input("Fatorial de qual número? \n"))
fat = calculaFatorial(v)
print("O fatorial de", v, "é", fat)