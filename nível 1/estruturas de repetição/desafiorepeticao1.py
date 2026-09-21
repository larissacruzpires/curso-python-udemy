# Desafio de Estrutas de Repetição - WHILE
# Exercício prátrico sobre loops

n = int(input("Digite um número: "))
soma = 0
while n != 0:
    soma = soma + (n % 10)
    n = (n // 10)
print(f"A soma entre estes números é {soma}.")