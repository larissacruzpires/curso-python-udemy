# Função com retorno

def um_megabit():
    valor = 1024 * 1024
    return valor

# def um_megabit():
# returno(1024 * 1024) -> otimização ao invés de usarmos a variável valor

#...

x = um_megabit()
print(f"O total de bits é: {x}")