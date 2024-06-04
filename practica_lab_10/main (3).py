class Jarra:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = 0

    def llenar(self):
        self.contenido = self.capacidad

    def vaciar(self):
        self.contenido = 0

    def transferir_a(self, otra_jarra):
        cantidad_transferir = min(self.contenido, otra_jarra.capacidad - otra_jarra.contenido)
        self.contenido -= cantidad_transferir
        otra_jarra.contenido += cantidad_transferir

def resolver_problema():
    jarra_5 = Jarra(5)
    jarra_3 = Jarra(3)
    
    pasos = []
    
    # Paso 1: Llenar la jarra de 5 litros
    jarra_5.llenar()
    pasos.append(f"Llenar jarra de 5 litros: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    # Paso 2: Verter el agua de la jarra de 5 litros a la jarra de 3 litros
    jarra_5.transferir_a(jarra_3)
    pasos.append(f"Transferir de 5L a 3L: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    # Paso 3: Vaciar la jarra de 3 litros
    jarra_3.vaciar()
    pasos.append(f"Vaciar jarra de 3 litros: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    # Paso 4: Verter el agua de la jarra de 5 litros a la jarra de 3 litros
    jarra_5.transferir_a(jarra_3)
    pasos.append(f"Transferir de 5L a 3L: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    # Paso 5: Llenar la jarra de 5 litros
    jarra_5.llenar()
    pasos.append(f"Llenar jarra de 5 litros: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    # Paso 6: Verter el agua de la jarra de 5 litros a la jarra de 3 litros
    jarra_5.transferir_a(jarra_3)
    pasos.append(f"Transferir de 5L a 3L: 5L, {jarra_5.contenido}L; 3L, {jarra_3.contenido}L")
    
    return pasos


if __name__ == "__main__":
    pasos_solucion = resolver_problema()
    for paso in pasos_solucion:
        print(paso)

