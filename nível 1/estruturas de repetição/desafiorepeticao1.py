# Desafio de Estrutas de Repetição - WHILE
# Exercício prátrico sobre loops

soma = 0
n = int(input("Digite um número: "))
while n != 0:
    soma = soma + (n % 10)
    n = (n // 10)
print(f"Resultado da soma entre estes números é {soma}.")
