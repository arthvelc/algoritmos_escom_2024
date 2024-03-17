import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import algoritmos

# Función para medir el tiempo de ejecución de un algoritmo
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def results_cli(array_sizes):
    for n in array_sizes:
        arr = random.sample(range(n), n)
        
        # Mergesort
        merge_sort_time = measure_time(algoritmos.merge_sort, arr.copy())
        print(f"Mergesort con n={n}: {merge_sort_time:.6f} segundos")

        # Quicksort
        quick_sort_time = measure_time(algoritmos.quick_sort, arr.copy())
        print(f"Quicksort con n={n}: {quick_sort_time:.6f} segundos")

        # Búsqueda binaria
        target = random.randint(0, n-1)
        arr.sort()
        binary_search_time = measure_time(algoritmos.binary_search, arr, target)
        print(f"Búsqueda binaria con n={n}: {binary_search_time:.10f} segundos")

        # Búsqueda ternaria
        ternary_search_time = measure_time(algoritmos.ternary_search, arr, target)
        print(f"Búsqueda ternaria con n={n}: {ternary_search_time:.10f} segundos")


def results_csv(array_sizes):
    # Listas para almacenar los tiempos de ejecución de cada algoritmo
    merge_sort_times = []
    quick_sort_times = []
    binary_search_times = []
    ternary_search_times = []
    
    for n in array_sizes:
        arr = random.sample(range(n), n)
        
        # Mergesort
        merge_sort_time = measure_time(algoritmos.merge_sort, arr.copy())
        merge_sort_times.append(merge_sort_time)
        
        # Quicksort
        quick_sort_time = measure_time(algoritmos.quick_sort, arr.copy())
        quick_sort_times.append(quick_sort_time)
        
        # Búsqueda binaria
        target = random.randint(0, n-1)
        arr.sort()
        binary_search_time = measure_time(algoritmos.binary_search, arr, target)
        binary_search_times.append(binary_search_time)
        
        # Búsqueda ternaria
        ternary_search_time = measure_time(algoritmos.ternary_search, arr, target)
        ternary_search_times.append(ternary_search_time)
    
    # Crear un DataFrame de pandas con los tiempos de ejecución
    data = {
        'Array Size': array_sizes,
        'Merge Sort': merge_sort_times,
        'Quick Sort': quick_sort_times,
        'Binary Search': binary_search_times,
        'Ternary Search': ternary_search_times
    }
    df = pd.DataFrame(data)
    
    # Guardar el DataFrame en un archivo CSV
    df.to_csv('./tiempos.csv', index=False)

    return array_sizes, merge_sort_times, quick_sort_times, binary_search_times, ternary_search_times
    

def results_plots(array_sizes, merge_sort_times, quick_sort_times, binary_search_times, ternary_search_times):
    # Generar los plots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot(array_sizes, merge_sort_times, label='Merge Sort', color='red')
    axs[0, 0].set_title('Merge Sort')
    axs[0, 0].set_xlabel('Array Size')
    axs[0, 0].set_ylabel('Execution Time (seconds)')
    axs[0, 0].grid(True)
    

    axs[0, 1].plot(array_sizes, quick_sort_times, label='Quick Sort', color = 'green')
    axs[0, 1].set_title('Quick Sort')
    axs[0, 1].set_xlabel('Array Size')
    axs[0, 1].set_ylabel('Execution Time (seconds)')
    axs[0, 1].grid(True)

    axs[1, 0].plot(array_sizes, binary_search_times, label='Binary Search', color = 'blue')
    axs[1, 0].set_title('Binary Search')
    axs[1, 0].set_xlabel('Array Size')
    axs[1, 0].set_ylabel('Execution Time (seconds)')
    axs[1, 0].grid(True)

    axs[1, 1].plot(array_sizes, ternary_search_times, label='Ternary Search', color = 'purple')
    axs[1, 1].set_title('Ternary Search')
    axs[1, 1].set_xlabel('Array Size')
    axs[1, 1].set_ylabel('Execution Time (seconds)')
    axs[1, 1].grid(True)

    plt.tight_layout()
    plt.savefig('./plot.png')
    print("Plots generados con éxito.")