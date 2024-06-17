import numpy as np
import random

def es_solucion(A, x, b, tol=1e-6):
    return np.allclose(np.dot(A, x), b, atol=tol)

def las_vegas_resolver(A, b, max_iteraciones=100):
    m, n = A.shape
    mejor_x = None
    mejor_error = float('inf')
    
    for _ in range(max_iteraciones):
        x = np.random.randint(-5, 6, n)  # Generar números enteros en el rango [-5, 5]
        error = np.linalg.norm(np.dot(A, x) - b)
        
        if error < mejor_error:
            mejor_error = error
            mejor_x = x
        
        if es_solucion(A, x, b):
            return x, error
    
    # Si no se encuentra una solución exacta, retornar la mejor aproximación
    return mejor_x, mejor_error

# Solicitar al usuario que ingrese el sistema de ecuaciones
def ingresar_sistema():
    m = int(input("Ingrese el número de ecuaciones (m): "))
    n = int(input("Ingrese el número de variables (n): "))
    
    print("Ingrese los coeficientes de la matriz A:")
    A = []
    for i in range(m):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        A.append(fila)
    
    A = np.array(A)
    
    print("Ingrese el vector b:")
    b = []
    for i in range(m):
        bi = float(input(f"b[{i+1}]: "))
        b.append(bi)
    
    b = np.array(b)
    
    return A, b

# Ejemplo de uso:
A, b = ingresar_sistema()
try:
    solucion, error = las_vegas_resolver(A, b)
    if error == 0:
        print(f'Solución exacta encontrada: {solucion}')
    else:
        print(f'No se encontró una solución exacta. Solución más cercana: {solucion} con error {error}')
except ValueError as e:
    print(e)
