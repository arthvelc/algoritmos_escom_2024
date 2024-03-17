import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import typer 
import click
import algoritmos
import logica_resultados

def main():
    # Generación de arreglos de números aleatorios
    array_sizes = [20, 100, 1000, 10000, 100000, 1000000, 5000000, 10000000]
    # Barra de progreso
    with typer.progressbar(range(100), label="Cargando programa...") as progress:
        for i in progress:
            time.sleep(0.01)

    # Barra de progreso
    with typer.progressbar(range(100), label="Procesando archivo CSV...") as progress:
        for i in progress:
            time.sleep(0.01)
    
    typer.echo(click.style("wait a moment...", fg="blue"))
    
    array_sizes, merge_sort_times, quick_sort_times, binary_search_times, ternary_search_times = logica_resultados.results_csv(array_sizes)

    # Barra de progreso
    with typer.progressbar(range(100), label="Procesando archivo png ...") as progress:
        for i in progress:
            time.sleep(0.01)

    logica_resultados.results_plots(array_sizes, merge_sort_times, quick_sort_times, binary_search_times, ternary_search_times)



    typer.echo(click.style("Programa finalizado con éxito. 😎👌", fg="green"))

if __name__ == "__main__":
    main()
    