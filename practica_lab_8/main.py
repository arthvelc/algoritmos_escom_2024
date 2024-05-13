def contar_formas(n, memo={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in memo:
        return memo[n]
    else:
        memo[n] = contar_formas(n - 1, memo) + contar_formas(n - 2, memo) + contar_formas(n - 3, memo)
        return memo[n]


# Código usando memorización
def contar_formas_memoization(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n in memo:
        return memo[n]
    else:
        memo[n] = contar_formas_memoization(n-1, memo) + contar_formas_memoization(n-2, memo) + contar_formas_memoization(n-3, memo)
        return memo[n]
    
if __name__ == "__main__":

    # Casos de prueba
    print('''
Ejemplo de uso:
        Utilizando el método de memoization para contar las formas de subir n escalones
    ''')
    casos_prueba = [2, 3, 4, 5, 6]
    for n in casos_prueba:
        print("Formas de subir", n, "escalones (Memoization):", contar_formas_memoization(n))