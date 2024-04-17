def min_moneda_cambio(V, monedas):
    n = len(monedas)
    resultado = []

    # Inicializar una lista para almacenar el número mínimo de monedas
    # necesarias para cada valor de 0 a V
    min_monedas = [0] + [float('inf')] * V

    # Inicializar una lista para almacenar el valor de la última moneda utilizada
    ultima_moneda = [-1] * (V + 1)

    # Calcular el número mínimo de monedas para cada valor de 1 a V
    for valor in range(1, V + 1):
        for i in range(n):
            if monedas[i] <= valor and min_monedas[valor - monedas[i]] + 1 < min_monedas[valor]:
                min_monedas[valor] = min_monedas[valor - monedas[i]] + 1
                ultima_moneda[valor] = i

    # Reconstruir la solución
    while V > 0:
        moneda = monedas[ultima_moneda[V]]
        resultado.append(moneda)
        V -= moneda

    return resultado

# Definir las monedas disponibles
monedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

# Calcular el cambio para diferentes valores de V
V1 = 2550
cambio_V1 = min_moneda_cambio(V1, monedas)
print("Cambio para V=2550:", cambio_V1)

V2 = 8432
cambio_V2 = min_moneda_cambio(V2, monedas)
print("Cambio para V=8432:", cambio_V2)

V3 = 263
cambio_V3 = min_moneda_cambio(V3, monedas)
print("Cambio para V=263:", cambio_V3)