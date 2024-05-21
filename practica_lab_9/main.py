def find_magic_index_simple(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1  # No se encontró un índice mágico



def find_magic_index_distinct(arr):
    def binary_search(arr, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return binary_search(arr, start, mid - 1)
        else:
            return binary_search(arr, mid + 1, end)
    
    return binary_search(arr, 0, len(arr) - 1)



def find_magic_index_non_distinct(arr):
    def binary_search(arr, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        
        # Busca en la mitad izquierda
        left_index = min(mid - 1, arr[mid])
        left = binary_search(arr, start, left_index)
        if left != -1:
            return left
        
        # Busca en la mitad derecha
        right_index = max(mid + 1, arr[mid])
        return binary_search(arr, right_index, end)
    
    return binary_search(arr, 0, len(arr) - 1)

def main(arr):
    print(f''' 
    Ejemplo de uso de las funcione de Magic Index:
        
        el arreglo es: {arr}

        Magic Index simple: {find_magic_index_simple(arr)}
        Magic Index distinct: {find_magic_index_distinct(arr)}
        Magic Index non distinct: {find_magic_index_non_distinct(arr)}
    ''')

if __name__ == '__main__':
    arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    main()