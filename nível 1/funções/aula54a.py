# Argumentos *ARGS
# retorna em tupla

def soma(*args):
    return sum(args)

print(soma(1,2,3,4,5,6,7))

# sem a função sum() - > total = 0
#     for i in args:
#         total += i