# Asignaciòn de memoria con el primer criterio voraz
def asignacion_bloques_caso1(bloques, procesos):
    asignaciones = []

    for proceso in procesos:
        for i, bloque in enumerate(bloques):
            if bloque >= proceso:
                # Asigna al primer bloque disponible que pueda contener el proceso
                asignaciones.append((proceso, i))
                bloques[i] -= proceso
                break

    return asignaciones


# Asisgnaciòn de memoria con el segundo criterio voraz
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
    # Ejemplo de la clase:
    bloques_memoria_clase = [150, 80, 120, 200]
    procesos_clase = [30, 100, 50, 70]

    print(f'''Asignaciones caso de la clase:
    
    La asignaciòn de la memoria en el primer caso es de:
    {asignacion_bloques_caso1(bloques_memoria_clase, procesos_clase)}

    La asignaciòn de la memoria en el segundo caso es de:
    {asignacion_bloques_caso2(bloques_memoria_clase, procesos_clase)}''')

    #Otros ejemplos:
    bloques_memoria = [100, 500, 200, 300, 600]
    procesos = [212, 417, 112, 426]

    print(f'''Asignaciones caso ejemplo 1:
          
    La asignaciòn de la memoria en el primer caso es de:
    {asignacion_bloques_caso1(bloques_memoria, procesos)}
    
    La asignaciòn de la memoria en el segundo caso es de:
    {asignacion_bloques_caso2(bloques_memoria, procesos)}''')

    bloques_memoria_2 = [100, 500, 200, 300, 600]
    procesos_2 = [212, 417, 112, 426, 112, 426]

    print(f'''Asignaciones caso ejemplo 2:
          
    La asignaciòn de la memoria en el primer caso es de:
    {asignacion_bloques_caso1(bloques_memoria_2, procesos_2)}

    La asignaciòn de la memoria en el segundo caso es de:
    {asignacion_bloques_caso2(bloques_memoria_2, procesos_2)}''')

    bloques_memoria_3 = [100, 500, 200, 300, 600]
    procesos_3 = [212, 417, 112, 426, 112, 426, 112, 426]

    print(f'''Asignaciones caso ejemplo 3:
          
    La asignaciòn de la memoria en el primer caso es de:
    {asignacion_bloques_caso1(bloques_memoria_3, procesos_3)}

    La asignaciòn de la memoria en el segundo caso es de:
    {asignacion_bloques_caso2(bloques_memoria_3, procesos_3)}''')
