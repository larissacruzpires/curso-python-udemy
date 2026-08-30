# Estrutura Condicional: Média de Nota

nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1+nota2)/2
if (media>=5):
    print("Esta é sua média", media,  ". Você está aprovado!")
else:
    print("Esta é sua média", media, ". Você está de recuperação!")