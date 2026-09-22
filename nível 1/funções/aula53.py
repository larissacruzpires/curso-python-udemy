# Documentando Funções com DocStrings

def potencia(numero, expoente=2):
    """ Função que calcula a potencia de um número
    Valor de Entrada:
    numero - número a ser calculado (elevado a potencia) (float)
    expoente - expoente a ser utilizado no cálculo (inteiro)

    Resultado:
    Resultado do cálculo de potencia (float)"""
    resultado = pow(numero, expoente)
    return resultado

#...
n = float(input("Digite o número: "))
e = int(input("Expoente: "))

print(f"Valor com expoente: {potencia(expoente=e,numero=n)}")
print(f"Valor sem expoente: {potencia(e)}")

print("-----------------------------------------------------")
help(potencia)

