# Dicionários (dict): apartamento

proprietarios = {}

while True:
    apto = int(input('Digite o apto: '))
    if apto != -1:
        proprietario = input("Proprietário: ")
        proprietarios.update({apto:proprietario})
    else:
        break

edificio = dict(sorted(proprietarios.items())) # conversão de list para dict

for chave, valor in  edificio.items():
    print(f"{chave} - {valor}")
print(f"Total de apartamentos: {len(edificio)}")
