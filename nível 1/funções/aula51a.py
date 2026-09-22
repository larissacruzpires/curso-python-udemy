# Função com parâmetros: área do círculo

def area_circulo(raio):
    PI = 3.141592
    area =  PI * pow(raio,2)
    return area

#...

r = float(input("Digite o valor do raio: "))
a = area_circulo(r)
print(f"O valor da área do circulo de raio {r} é igual a {a}")