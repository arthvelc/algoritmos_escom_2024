def mochila_fraccionaria(items, capacidad):
    # Calcula la razón valor/peso para cada artículo
    ratios = [(item[0] / item[1], item) for item in items]
    # Ordena los artículos en función de las razones
    ratios.sort(reverse=True)
    
    total_valor = 0
    mochila = []

    for ratio, (valor, peso) in ratios:
        if capacidad >= peso:
            # Si cabe el artículo completo, lo añade a la mochila
            mochila.append((valor, peso))
            total_valor += valor
            capacidad -= peso
        else:
            # Si no cabe completo, añade una fracción del artículo
            fraccion = capacidad / peso
            mochila.append((valor * fraccion, peso * fraccion))
            total_valor += valor * fraccion
            break  # Termina el bucle

    return total_valor, mochila


if __name__ == "__main__":
    items = [(10, 2), (20, 5), (30, 10)]
    capacidad= 15

    print(f'''
          
          Mochila fraccionaria Ejemplo 1:
          
          ''')
    total_valor, mochila = mochila_fraccionaria(items, capacidad)
    print("Valor total en la mochila:", total_valor)
    print("Contenido de la mochila:")
    for valor, peso in mochila:
        print(f"  Valor: {valor}, Peso: {peso}")

    items_2 = [(25, 5), (40, 10), (35, 8)]
    capacidad_2= 20

    print(f'''
          
          Mochila fraccionaria Ejemplo 2:
          
          ''')

    total_valor_2, mochila_2 = mochila_fraccionaria(items_2, capacidad_2)
    print("Valor total en la mochila:", total_valor_2)
    print("Contenido de la mochila:")
    for valor, peso in mochila_2:
        print(f"  Valor: {valor}, Peso: {peso}")
    
