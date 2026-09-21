# Conjuntos (sets): lista

palavras = []
lista = []

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == '':
        break
    else:
        palavras.append(palavra)

for palavra in palavras:
    lista.append(list(set(palavra)))

for item in lista:
    print(item)