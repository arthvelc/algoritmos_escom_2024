import time
import sys

def mochila_01(pesos, valores, capacidad):
    n = len(pesos)
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    memoria_usada = (sys.getsizeof(pesos) + sys.getsizeof(valores) + sys.getsizeof(capacidad) + sys.getsizeof(dp)) / 1024  # Uso de memoria en KB
    return dp[n][capacidad], memoria_usada

def print_table(data, headers):
    row_format ="{:<15}" * (len(headers))
    print(row_format.format(*headers))
    for row in data:
        print(row_format.format(*row))

escenarios = [
    (4, [1, 2, 3], [10, 20, 30]),
    (10, [2, 3, 5, 7], [1, 4, 5, 7]),
    (15, [3, 4, 6, 8], [2, 3, 1, 5]),
    (10, [5, 5, 5], [10, 20, 30]),
    (5, [6, 7, 8], [10, 12, 15])
]

resultados = []
for capacidad, pesos, valores in escenarios:
    inicio = time.time()
    resultado, memoria_usada = mochila_01(pesos, valores, capacidad)
    fin = time.time()
    tiempo_transcurrido = (fin - inicio) * 1000  # Tiempo en ms
    resultados.append([str(capacidad), str(pesos), str(valores), str(resultado), f"{tiempo_transcurrido:.2f} ms", f"{memoria_usada:.2f} KB"])

headers = ["Capacidad", "Pesos", "Valores", "Resultado", "Tiempo", "Memoria"]
print_table(resultados, headers)
