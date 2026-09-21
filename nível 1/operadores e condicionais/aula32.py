# Comando elif (controle de decisão multidirecional): Nota

nota = float(input("Nota: "))
if (nota<0) or (nota>1):
    print("Entrada Incorreta!")
elif nota>=0.9:
    print("Conceito A")
elif nota>=0.8:
    print("Conceito B")
elif nota>=0.7:
    print("Conceito C")
elif nota >=0.6:
    print("Conceito D")
else:
    print("Conceito F")