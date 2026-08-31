# Estrutura Condicional: Segundo Desafio
# Peso Ideal

h = float(input("Digite a sua altura exata: "))
sexo = (input("Qual o seu sexo <F ou M>: "))

if (sexo == 'M'):
    pesoideal = float((h * 72.7 - 58) // 1)

else:
     pesoideal = float((h * 62.1 - 44.7) //1)
print(pesoideal, " é o seu peso ideal!")
