# Argumentos **KWARGS
# retorna em dicionário

def comida_favorita(**kwargs):
   for chave in kwargs:
       print(f"{chave} gosta de {kwargs[chave]}")

comida_favorita(ana="bacalhoada", marcelo="risoto", adriana="camarão a baiana")


# parâmetros em ordem?
# 1 - parâmetros definidos
# 2 - *args
# 3 - parâmetros nomeados
# 4 - **kwargs

# se utilizamos esta ordem -> def comida_favorita(a, b, *args, c=3, **kwargs):
