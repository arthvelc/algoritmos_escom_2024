def encontrar_mayor_raiz_cuadrada(X):
    # Casos base
    if X == 0 or X == 1:
        return X

    # Inicializar límite inferior y límite superior
    l = 0
    r = X // 2

    # Inicializar respuesta
    ans = 0

    # Búsqueda binaria
    while l <= r:
        mid = (l + r) // 2
        cuadrado = mid * mid

        # Si el cuadrado de mid es menor o igual a X, buscar en la segunda mitad
        if cuadrado <= X:
            ans = mid
            l = mid + 1
        # Si el cuadrado de mid es mayor que X, buscar en la primera mitad
        else:
            r = mid - 1
    return ans

X = int(input("Ingrese un número: "))
print("El entero mayor cuyo cuadrado es menor o igual a", X, "es", encontrar_mayor_raiz_cuadrada(X))