#include <stdio.h>

int encontrar_mayor_raiz_cuadrada(int X) {
    // Casos base
    if (X == 0 || X == 1) {
        return X;
    }

    // Inicializar límite inferior y límite superior
    int l = 0;
    int r = X / 2;

    // Inicializar respuesta
    int ans = 0;

    // Búsqueda binaria
    while (l <= r) {
        int mid = (l + r) / 2;
        int cuadrado = mid * mid;

        // Si el cuadrado de mid es menor o igual a X, buscar en la segunda mitad
        if (cuadrado <= X) {
            ans = mid;
            l = mid + 1;
        } 
        // Si el cuadrado de mid es mayor que X, buscar en la primera mitad
        else {
            r = mid - 1;
        }
    }
    return ans;
}

int main() {
    int X;
    printf("Ingrese un número: ");
    scanf("%d", &X);
    
    printf("El entero mayor cuyo cuadrado es menor o igual a %d es %d\n", X, encontrar_mayor_raiz_cuadrada(X));
    return 0;
}