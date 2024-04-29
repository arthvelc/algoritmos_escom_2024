def capturar_ladrones(arr, k):
    n = len(arr)
    policia = ladron = 0
    asignaciones = 0

    while policia < n and ladron < n:
        # Si el ladron está dentro del rango de captura del policía
        if abs(ladron - policia) <= k:
            asignaciones += 1
            # Encontrar el próximo policía y ladron
            next_index = max(policia, ladron) + 1
            while next_index < n and arr[next_index] != ('P' if arr[policia] == 'P' else 'L'):
                next_index += 1
            if next_index == n:
                break
            policia = ladron = next_index
        else:
            # Incrementar el índice del próximo policía o ladron
            min_index = min(policia, ladron)
            next_index = min_index + 1
            while next_index < n and arr[next_index] != ('P' if arr[policia] == 'P' else 'L'):
                next_index += 1
            if next_index == n:
                break
            policia = ladron = next_index

    return asignaciones

# Ejemplo de uso

print("Ejemplo 1:")
arr = ['P', 'L', 'L', 'P', 'L', 'P']
k = 1
print("Número de ladrones capturados:", capturar_ladrones(arr, k))
print()
print("Ejemplo 2:")
arr_2 = ['P', 'L', 'L', 'P', 'L', 'P', 'L', 'L', 'P', 'P', 'L', 'P', 'L', 'P']
k = 2
print("Número de ladrones capturados:", capturar_ladrones(arr_2, k))
print()
print("Ejemplo 3:")
arr_3 = ['P', 'L', 'L', 'P', 'L', 'P', 'L', 'L', 'P', 'P', 'L', 'P', 'L', 'P']
k = 3
print("Número de ladrones capturados:", capturar_ladrones(arr_3, k))
print()
print("Ejemplo 4:")
arr_4= ['P','P','P','P','P', 'L', 'P', 'L', 'L', 'P', 'P', 'L', 'P',]
k = 4
print("Número de ladrones capturados:", capturar_ladrones(arr_4, k))