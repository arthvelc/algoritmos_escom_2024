def asignacion_memoria_voraz_1(bloques_memoria, procesos):
    asignaciones = []
    for proceso in procesos:
        asignado = False
        for i, bloque in enumerate(bloques_memoria):
            print(i)
            print(bloque)
            if bloque >= proceso:
                asignaciones.append((proceso, i))
                bloques_memoria[i] -= proceso
                asignado = True
                break
        if not asignado:
            asignaciones.append((proceso, -1))
    return asignaciones

def asignacion_memoria_voraz_2(bloques_memoria, procesos):
    asignaciones = []
    for proceso in procesos:
        asignado = False
        max_bloque = -1
        max_tam = 0
        for i, bloque in enumerate(bloques_memoria):
            if bloque >= proceso and bloque > max_tam:
                max_bloque = i
                max_tam = bloque
                asignado = True
        if asignado:
            asignaciones.append((proceso, max_bloque))
            bloques_memoria[max_bloque] -= proceso
        else:
            asignaciones.append((proceso, -1))
    return asignaciones

if __name__ == '__main__':
    bloques_memoria = [100, 500, 200, 300, 600]
    procesos = [212, 417, 112, 426]
    asignacion_1 = asignacion_memoria_voraz_1(bloques_memoria, procesos)
    
