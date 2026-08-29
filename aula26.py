TIPO STRING (CHAR ou caracter)
ATENÇÃO: 1 ou mais caracteres = STRING
ATENÇÃO 2: s = 'a' ou "a"  -> sem quebra de linha
           s = '''a'''  ou  """a"""   -> com quebra de linha
-----------------------------------------------------------
letra='a'
palavra='pyPRO'
type(letra)
type(palavra)
frase="Seja um profissional Python!"
print(frase)

print(frase[1])

frase2=['S','e','j','a',' ','u','m',' ','p']
print(frase2[1])

#Slices de strings
print(frase[0:4])

#Slice de strings: 3 parâmetros:
#1 - início
#2 - limite superior (ele pegará até o n-1)
#3 - tamanho do passo (se deixar em branco, passo igual a 1)
print(frase[0:15:1])
print(frase[0:15:2])
print(frase[15:0:-1])
print(frase[15::-1])
print(frase[::-1])

dir(frase)
print(frase.split())
print(frase.split()[2])
print(frase.uper())
print(frase.lower())
print(frase.swapcase())

frase2 = '    Texto   '
print(frase2)
print(frase2.strip())

