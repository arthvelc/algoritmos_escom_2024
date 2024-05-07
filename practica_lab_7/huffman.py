'''Parte 1. Codificación de Huffman.
Genera un programa que pida al usuario capturar un texto. Dicho texto tendrá que ser procesado de tal manera que se generen las frecuencias de ocurrencia de cada letra (incluidos los espacios), posteriormente genera la codificación de Huffman correspondiente y codifica el texto capturado. 

Almacena el texto original y codificado en archivos separados.

Parte 2: Decodificación Huffman.

Averigua en qué consiste el algoritmo de decodificación del código Huffman, e incorpóralo en el programa de la primera parte. Prueba con el mismo texto de entrada.'''

def huffman(texto):
    # Genera la tabla de frecuencias
    tabla = {}
    for letra in texto:
        if letra in tabla:
            tabla[letra] += 1
        else:
            tabla[letra] = 1

    print(f'Tabla de frecuencias: {tabla}')
    # Genera el árbol de Huffman
    arbol = []

    for letra in tabla:
        arbol.append((tabla[letra], letra))
    arbol.sort()

    print(f'Árbol de Huffman: {arbol}')
    while len(arbol) > 1:
        peso1, letra1 = arbol.pop(0)
        peso2, letra2 = arbol.pop(0)
        arbol.append((peso1 + peso2, letra1 + letra2))
        arbol.sort()

    print(f'Árbol de Huffman: {arbol}')
    arbol = arbol[0][1]
    print(f'Árbol de Huffman: {arbol}')

    # Genera la tabla de códigos
    tabla = {}
    for letra in arbol:
        
        tabla[letra] = ''
    print(f'Tabla de códigos: {tabla}')
# Tengo que ver que pedo con la tabla de códigos siempre se va a == 1
    for letra in arbol:
        if len(letra) == 1:
            tabla[letra] = '0'
        else:
            for i in letra:
                tabla[i] = '1' + tabla[i]
    
    print(f'Tabla de códigos: {tabla}')

    # Codifica el texto
    texto_codificado = ''
    for letra in texto:
        texto_codificado += tabla[letra]
    
    #return texto_codificado

def decodifica_huffman(texto_codificado, arbol):
    texto = ''
    nodo = arbol
    for bit in texto_codificado:
        if bit == '0':
            nodo = nodo[0]
        else:
            nodo = nodo[1]
        if len(nodo) == 1:
            texto += nodo
            nodo = arbol
    return texto

if __name__ == '__main__':
    texto = input('Introduce un texto: ')
    huffman(texto)
