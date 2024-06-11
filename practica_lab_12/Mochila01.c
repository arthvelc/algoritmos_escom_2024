#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <string.h> // Para usar strcat

int mochila01(int* pesos, int* valores, int n, int capacidad) {
    int** dp = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)malloc((capacidad + 1) * sizeof(int));
    }

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacidad; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (pesos[i - 1] <= w) {
                dp[i][w] = dp[i - 1][w] > dp[i - 1][w - pesos[i - 1]] + valores[i - 1] ? dp[i - 1][w] : dp[i - 1][w - pesos[i - 1]] + valores[i - 1];
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    int resultado = dp[n][capacidad];

    for (int i = 0; i <= n; i++) {
        free(dp[i]);
    }
    free(dp);

    return resultado;
}

void printTable(char* data[5][6]) {
    char* headers[] = {"Capacidad", "Pesos", "Valores", "Resultado", "Tiempo", "Memoria"};
    for (int i = 0; i < 6; i++) {
        printf("%s\t", headers[i]);
    }
    printf("\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            printf("%s\t", data[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int capacidades[5] = {4, 10, 15, 10, 5};
    int pesos[5][4] = {
        {1, 2, 3, 0},
        {2, 3, 5, 7},
        {3, 4, 6, 8},
        {5, 5, 5, 0},
        {6, 7, 8, 0}
    };
    int valores[5][4] = {
        {10, 20, 30, 0},
        {1, 4, 5, 7},
        {2, 3, 1, 5},
        {10, 20, 30, 0},
        {10, 12, 15, 0}
    };

    char* resultados[5][6];

    for (int i = 0; i < 5; i++) {
        int capacidad = capacidades[i];
        int n = sizeof(pesos[i]) / sizeof(pesos[i][0]);
        while (pesos[i][n-1] == 0) n--; // Determinar el tamaño real de la fila

        clock_t inicio = clock();
        int resultado = mochila01(pesos[i], valores[i], n, capacidad);
        clock_t fin = clock();
        double tiempoTranscurrido = (double)(fin - inicio) / CLOCKS_PER_SEC * 1000; // Tiempo en ms

        // Medición de memoria no es precisa en C como en otros lenguajes, se usa una estimación simple
        int memoriaUsada = (sizeof(int) * (capacidad + 1) * (n + 1) + sizeof(pesos[i]) + sizeof(valores[i]) + sizeof(capacidad)) / 1024; // KB

        resultados[i][0] = (char*)malloc(20 * sizeof(char));
        resultados[i][1] = (char*)malloc(50 * sizeof(char));
        resultados[i][2] = (char*)malloc(50 * sizeof(char));
        resultados[i][3] = (char*)malloc(20 * sizeof(char));
        resultados[i][4] = (char*)malloc(20 * sizeof(char));
        resultados[i][5] = (char*)malloc(20 * sizeof(char));

        sprintf(resultados[i][0], "%d", capacidad);
        char pesos_str[50];
        sprintf(pesos_str, "[");
        for (int j = 0; j < n; j++) {
            char buffer[5];
            sprintf(buffer, "%d", pesos[i][j]);
            strcat(pesos_str, buffer);
            if (j < n - 1) {
                strcat(pesos_str, ", ");
            }
        }
               strcat(pesos_str, "]");
        sprintf(resultados[i][1], "%s", pesos_str);

        char valores_str[50];
        sprintf(valores_str, "[");
        for (int j = 0; j < n; j++) {
            char buffer[5];
            sprintf(buffer, "%d", valores[i][j]);
            strcat(valores_str, buffer);
            if (j < n - 1) {
                strcat(valores_str, ", ");
            }
        }
        strcat(valores_str, "]");
        sprintf(resultados[i][2], "%s", valores_str);

        sprintf(resultados[i][3], "%d", resultado);
        sprintf(resultados[i][4], "%.2f ms", tiempoTranscurrido);
        sprintf(resultados[i][5], "%d KB", memoriaUsada);
    }

    printTable(resultados);

    // Liberar memoria
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            free(resultados[i][j]);
        }
    }

    return 0;
}
