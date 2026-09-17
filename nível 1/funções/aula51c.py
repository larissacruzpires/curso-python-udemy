# Função com parâmetros: Teste

def area_cilindro(raio, altura):

    def area_circulo(raio):
        PI = 3.141592
        area = PI * pow(raio, 2)
        return area

    area = area_circulo(raio) * altura
    return area
#...

r = float(input("Digite o valor do raio: "))
h = float(input("Digite a altura do cilindro: "))
a = area_cilindro(r, h)
print(f"O valor da área do cilindro é {a}")
# print("-----------------------------")
# ac = area_circulo(r) --> a variável area_circulo só é reconhecida no primeiro bloco
# print(f"O valor da área do círculo é {ac}")