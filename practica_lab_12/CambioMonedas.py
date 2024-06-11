import time
import sys

def cambio_monedas(monedas, cantidad):
    dp = [float('inf')] * (cantidad + 1)
    dp[0] = 0
    for moneda in monedas:
        for x in range(moneda, cantidad + 1):
            dp[x] = min(dp[x], dp[x - moneda] + 1)
    memoria_usada = (sys.getsizeof(monedas) + sys.getsizeof(cantidad) + sys.getsizeof(dp)) / 1024  # Uso de memoria en KB
    return dp[cantidad] if dp[cantidad] != float('inf') else -1, memoria_usada

def print_table(data, headers):
    row_format ="{:<15}" * (len(headers))
    print(row_format.format(*headers))
    for row in data:
        print(row_format.format(*row))

escenarios = [
    (11, [1, 2, 5]),
    (30, [1, 2, 5, 10]),
    (99, [1, 5, 10, 25, 50]),
    (3, [2, 5, 10]),
    (7, [2, 4])
]

resultados = []
for cantidad, monedas in escenarios:
    inicio = time.time()
    resultado, memoria_usada = cambio_monedas(monedas, cantidad)
    fin = time.time()
    tiempo_transcurrido = (fin - inicio) * 1000  # Tiempo en ms
    resultados.append([str(cantidad), str(monedas), str(resultado), f"{tiempo_transcurrido:.2f} ms", f"{memoria_usada:.2f} KB"])

headers = ["Cantidad", "Monedas", "Resultado", "Tiempo", "Memoria"]
print_table(resultados, headers)
