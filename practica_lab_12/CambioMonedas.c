#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <string.h> // Para usar strcat

int cambioMonedas(int* monedas, int tam, int cantidad) {
    int* dp = (int*)malloc((cantidad + 1) * sizeof(int));
    for (int i = 0; i <= cantidad; i++) {
        dp[i] = INT_MAX;
    }
    dp[0] = 0;

    for (int i = 0; i < tam; i++) {
        for (int j = monedas[i]; j <= cantidad; j++) {
            if (dp[j - monedas[i]] != INT_MAX) {
                dp[j] = dp[j] < dp[j - monedas[i]] + 1 ? dp[j] : dp[j - monedas[i]] + 1;
            }
        }
    }

    int resultado = dp[cantidad] == INT_MAX ? -1 : dp[cantidad];
    free(dp);
    return resultado;
}

void printTable(char* data[5][5]) {
    char* headers[] = {"Cantidad", "Monedas", "Resultado", "Tiempo", "Memoria"};
    for (int i = 0; i < 5; i++) {
        printf("%s\t", headers[i]);
    }
    printf("\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%s\t", data[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int escenarios[5][5] = {
        {11, 1, 2, 5},
        {30, 1, 2, 5, 10},
        {99, 1, 5, 10, 25},
        {3, 2, 5, 10},
        {7, 2, 4}
    };

    char* resultados[5][5];

    for (int i = 0; i < 5; i++) {
        int cantidad = escenarios[i][0];
        int* monedas = &escenarios[i][1];
        int tam = (sizeof(escenarios[i]) / sizeof(escenarios[i][1])) - 1;

        clock_t inicio = clock();
        int resultado = cambioMonedas(monedas, tam, cantidad);
        clock_t fin = clock();
        double tiempoTranscurrido = (double)(fin - inicio) / CLOCKS_PER_SEC * 1000; // Tiempo en ms

        // Medición de memoria no es precisa en C como en otros lenguajes, se usa una estimación simple
        int memoriaUsada = (sizeof(int) * (cantidad + 1) + sizeof(monedas) + sizeof(cantidad)) / 1024; // KB

        resultados[i][0] = (char*)malloc(20 * sizeof(char));
        resultados[i][1] = (char*)malloc(50 * sizeof(char));
        resultados[i][2] = (char*)malloc(20 * sizeof(char));
        resultados[i][3] = (char*)malloc(20 * sizeof(char));
        resultados[i][4] = (char*)malloc(20 * sizeof(char));

        sprintf(resultados[i][0], "%d", cantidad);
        char monedas_str[50];
        sprintf(monedas_str, "[");
        for (int j = 0; j < tam; j++) {
            char buffer[5];
            sprintf(buffer, "%d", monedas[j]);
            strcat(monedas_str, buffer);
            if (j < tam - 1) {
                strcat(monedas_str, ", ");
            }
        }
        strcat(monedas_str, "]");
        sprintf(resultados[i][1], "%s", monedas_str);
        sprintf(resultados[i][2], "%d", resultado);
        sprintf(resultados[i][3], "%.2f ms", tiempoTranscurrido);
        sprintf(resultados[i][4], "%d KB", memoriaUsada);
    }

    printTable(resultados);

    // Liberar memoria
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            free(resultados[i][j]);
        }
    }

    return 0;
}
