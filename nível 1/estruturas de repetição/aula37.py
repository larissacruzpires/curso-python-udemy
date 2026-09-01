# Comando for e Função ranger

soma = 0
for i in range(1,6):
    idade = int(input(f"Entre com a idade {i}: "))
    soma = soma + idade
media = soma/5
print("A média das idades é: ", media)