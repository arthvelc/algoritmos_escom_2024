import random
import time
import pandas as pd

def buscar_un_arreglo(A, t):
    for i in range(len(A)):
        if A[i] == t:
            return True
    return False

def buscar_dos_arreglos(A, B, t):
    for i in range(len(A)):
        if A[i] == t:
            return True
    for i in range(len(B)):
        if B[i] == t:
            return True
    return False

def verificar_elemento_comun(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return True
    return False

def verificar_duplicados(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False

def main():
    # Generar arreglos aleatorios
    valores_n = [10, 100, 1000, 10000, 1000000]
    arreglos = []
    for n in valores_n:
        arreglo = [random.randint(1, 100) for _ in range(n)]
        arreglos.append(arreglo)

    # Medir el tiempo de ejecución para cada algoritmo y tamaño de entrada
    resultados = []
    for i in range(len(valores_n)):
        n = valores_n[i]
        arreglo = arreglos[i]

        tiempo_inicio = time.time()
        buscar_un_arreglo(arreglo, 42)
        tiempo_fin = time.time()
        tiempo_buscar_un_arreglo = tiempo_fin - tiempo_inicio

        tiempo_inicio = time.time()
        buscar_dos_arreglos(arreglo, arreglo, 42)
        tiempo_fin = time.time()
        tiempo_buscar_dos_arreglos = tiempo_fin - tiempo_inicio

        tiempo_inicio = time.time()
        verificar_elemento_comun(arreglo, arreglo)
        tiempo_fin = time.time()
        tiempo_verificar_elemento_comun = tiempo_fin - tiempo_inicio

        tiempo_inicio = time.time()
        verificar_duplicados(arreglo)
        tiempo_fin = time.time()
        tiempo_verificar_duplicados = tiempo_fin - tiempo_inicio

        resultados.append([tiempo_buscar_un_arreglo, tiempo_buscar_dos_arreglos, tiempo_verificar_elemento_comun, tiempo_verificar_duplicados])

    # Crear un DataFrame de pandas para presentar los resultados
    df = pd.DataFrame(resultados, columns=['buscar un arreglo', 'buscar dos arreglos', 'verificar elemento comun', 'verificar duplicados'])
    df.insert(0, 'n', valores_n)
    # Guardar los resultados en un archivo CSV
    df.to_csv('/home/artur/ESCOM/ADA/Practica_lab_1/results.csv', index=False)

    print('Resultados guardados en el archivo CSV de manera exitosa.')

if __name__ == '__main__':
    main()