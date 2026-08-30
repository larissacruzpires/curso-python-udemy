# Estrutura Condicional: Primeiro Desafio
# O Número é par ou ímpar?

n = int(input("Digite um número inteiro e positivo: "))
if n > 0:
    if (n % 2) == 0:
        print(n, " é um número par!")
    else:
        print(n, " é um número ímpar!")
else:
    print("O número digitado é igual ou menor que zero!")
