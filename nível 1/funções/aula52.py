# Função com parâmetro padrão
# quando um parâmetro pode ser omitido

def potencia(numero, expoente=2):
    resultado = pow(numero, expoente)
    return resultado

#...
n = float(input("Digite o número: "))
e = int(input("Expoente: "))

print(f"Valor com expoente: {potencia(expoente=e,numero=n)}")
print(f"Valor sem expoente: {potencia(n)}")