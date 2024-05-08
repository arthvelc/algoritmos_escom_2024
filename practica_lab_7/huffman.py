import heapq
import os

'''Utilizaré la programación orientada a objetos para implementar el algoritmo de Huffman.

También utilizaré la librería heapq para manejar la cola de prioridad necesaria para el algoritmo.

También la librería os para manejar la lectura y escritura de archivos.'''


# Clase NodoHuffman: Representa un nodo en el árbol de Huffman.
class NodoHuffman:
    # Atributos del nodo Huffman
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    # Método __lt__: Compara dos nodos Huffman por frecuencia.
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


# Clase CodificadorHuffman: Codifica y decodifica texto utilizando el algoritmo de Huffman.
class CodificadorHuffman:
    # Genera un diccionario de frecuencias de caracteres en un texto.
    def generar_frecuencias(self, texto):
        frecuencias = {}
        for caracter in texto:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        return frecuencias

    # Genera un árbol de Huffman a partir del diccionario de frecuencias.
    def generar_arbol_huffman(self, frecuencias):
        cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
        heapq.heapify(cola_prioridad)
        while len(cola_prioridad) > 1:
            nodo_izq = heapq.heappop(cola_prioridad)
            nodo_der = heapq.heappop(cola_prioridad)
            nodo_combinado = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
            nodo_combinado.izquierda = nodo_izq
            nodo_combinado.derecha = nodo_der
            heapq.heappush(cola_prioridad, nodo_combinado)
        return cola_prioridad[0]
    
    # Genera un diccionario de códigos de Huffman a partir del árbol de Huffman.
    def generar_codigos_huffman(self, nodo, prefijo="", codigos={}):
        if nodo is not None:
            if nodo.caracter is not None:
                codigos[nodo.caracter] = prefijo
            self.generar_codigos_huffman(nodo.izquierda, prefijo + "0", codigos)
            self.generar_codigos_huffman(nodo.derecha, prefijo + "1", codigos)
        return codigos

    # Codifica un texto utilizando un diccionario de códigos de Huffman.
    def codificar_texto(self, texto, codigos):
        texto_codificado = ""
        for caracter in texto:
            texto_codificado += codigos[caracter]
        return texto_codificado

    # Decodifica un texto codificado utilizando un árbol de Huffman.
    def decodificar_texto(self, texto_codificado, arbol_huffman):
        texto_decodificado = ""
        nodo_actual = arbol_huffman
        for bit in texto_codificado:
            if bit == '0':
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
            if nodo_actual.caracter is not None:
                texto_decodificado += nodo_actual.caracter
                nodo_actual = arbol_huffman
        return texto_decodificado

# Función main: Pide al usuario un texto, lo codifica y lo decodifica.
def main():
    codificador = CodificadorHuffman()

    # Parte 1: Codificación de Huffman
    texto = input("Introduce el texto a codificar: ")
    frecuencias = codificador.generar_frecuencias(texto)
    arbol_huffman = codificador.generar_arbol_huffman(frecuencias)
    codigos = codificador.generar_codigos_huffman(arbol_huffman)
    texto_codificado = codificador.codificar_texto(texto, codigos)

    with open("./practica_lab_7/texto_original.txt", "w") as archivo_original:
        archivo_original.write(texto)

    with open("./practica_lab_7/texto_codificado.txt", "w") as archivo_codificado:
        archivo_codificado.write(texto_codificado)

    # Parte 2: Decodificación de Huffman
    texto_codificado_leido = ""
    with open("./practica_lab_7/texto_codificado.txt", "r") as archivo_codificado:
        texto_codificado_leido = archivo_codificado.read()

    texto_decodificado = codificador.decodificar_texto(texto_codificado_leido, arbol_huffman)
    print("Texto decodificado:", texto_decodificado)

if __name__ == "__main__":
    main()

