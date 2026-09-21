# Listas (list): Cidade

cidades = []

while True:
    cidade = input("Digite uma cidade: ")
    if cidade == 'sair':
        break
    else:
        cidades.append(cidade)

if len(cidades) > 0:
    cidades.sort()

    for cidade in cidades:
        print(cidade)
else:
    print("A lista de cidades está vazia!")