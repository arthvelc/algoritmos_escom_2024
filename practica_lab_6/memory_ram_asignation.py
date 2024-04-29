
def asignacion_bloques_caso2(bloques, procesos):
    asignaciones = []

    for proceso in procesos:
        mejor_espacio = max(bloques)
        mejor_indice = bloques.index(mejor_espacio)

        for i, bloque in enumerate(bloques):
            if bloque >= proceso and bloque < mejor_espacio:
                mejor_espacio = bloque
                mejor_indice = i

        asignaciones.append((proceso, mejor_indice))
        bloques[mejor_indice] -= proceso

    return asignaciones

if __name__ == '__main__':
    bloques_memoria = [100, 500, 200, 300, 600]
    procesos = [212, 417, 112, 426]
    asignacion_1 = asignacion_bloques_caso2(bloques_memoria, procesos)

    bloques_memoria_2 = [500,600,200,300,100]
    procesos_2 = [456,354,123,567]
    asignacion_2 = asignacion_bloques_caso2(bloques_memoria_2, procesos_2)

    bloques_memoria_3 = [100, 500, 200, 300, 600]
    procesos_3 = [100,150,500,200,300,600]
    asignacion_3 = asignacion_bloques_caso2(bloques_memoria_3, procesos_3)

    print(f'''Caso 1:
    bloques_memoria = [100, 500, 200, 300, 600]
    procesos = [212, 417, 112, 426]
    Asignaciones: {asignacion_1}
    
Caso 2:
    bloques_memoria = [500,600,200,300,100]
    procesos = [456,354,123,567]
    Asignaciones: {asignacion_2}
    
Caso 3:
    bloques_memoria = [100, 500, 200, 300, 600]
    procesos = [100,150,500,200,300,600]
    Asignaciones: {asignacion_3}''')