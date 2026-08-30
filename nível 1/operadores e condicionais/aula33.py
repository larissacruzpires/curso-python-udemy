# Aninhamento de Estruturas Condicionais

n = int(input("Entre com um número: "))

if(n >= 0):
    if(n % 2) == 0:
        print(n, " é par positivo!")
    else:
        print(n, " é impar positivo!")
else:
    if (abs(n) % 2) == 0:
        print(n, " é par negativo!")
    else:
        print(n, " é impar negativo")
