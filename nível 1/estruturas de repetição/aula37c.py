# Comando for
# Cálculo fatorial de um número

n = int(input("Entre com um número inteiro positivo: "))
fatorial = 1
if n < 0:
    print("Fatorial não existe!")
elif n == 0:
    print("Fatorial de 0 é igual a 1.")
else:
    for i in range(1, n+1):
        fatorial = fatorial * i
    print(f"Fatorial de {n} é igual a {fatorial}.")