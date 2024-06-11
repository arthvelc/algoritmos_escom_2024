import java.util.Arrays;

public class Mochila01 {
    public static int mochila01(int[] pesos, int[] valores, int capacidad) {
        int n = pesos.length;
        int[][] dp = new int[n + 1][capacidad + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacidad; w++) {
                if (pesos[i - 1] <= w) {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][capacidad];
    }

    public static long calcularMemoriaUsada() {
        Runtime runtime = Runtime.getRuntime();
        runtime.gc();
        return (runtime.totalMemory() - runtime.freeMemory()) / 1024; // KB
    }

    public static void printTable(String[][] data, String[] headers) {
        for (String header : headers) {
            System.out.print(header + "\t");
        }
        System.out.println();
        for (String[] row : data) {
            for (String cell : row) {
                System.out.print(cell + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] capacidadesPesosValores = {
            {4, 1, 2, 3, 10, 20, 30},
            {10, 2, 3, 5, 7, 1, 4, 5, 7},
            {15, 3, 4, 6, 8, 2, 3, 1, 5},
            {10, 5, 5, 5, 10, 20, 30},
            {5, 6, 7, 8, 10, 12, 15}
        };

        String[][] resultados = new String[capacidadesPesosValores.length][6];
        String[] headers = {"Capacidad", "Pesos", "Valores", "Resultado", "Tiempo", "Memoria"};

        for (int i = 0; i < capacidadesPesosValores.length; i++) {
            int capacidad = capacidadesPesosValores[i][0];
            int[] pesos = Arrays.copyOfRange(capacidadesPesosValores[i], 1, (capacidadesPesosValores[i].length / 2) + 1);
            int[] valores = Arrays.copyOfRange(capacidadesPesosValores[i], (capacidadesPesosValores[i].length / 2) + 1, capacidadesPesosValores[i].length);

            long inicio = System.nanoTime();
            int resultado = mochila01(pesos, valores, capacidad);
            long fin = System.nanoTime();
            long tiempoTranscurrido = (fin - inicio) / 1000000; // Tiempo en ms

            long memoriaUsada = calcularMemoriaUsada();

            resultados[i][0] = String.valueOf(capacidad);
            resultados[i][1] = Arrays.toString(pesos);
            resultados[i][2] = Arrays.toString(valores);
            resultados[i][3] = String.valueOf(resultado);
            resultados[i][4] = tiempoTranscurrido + " ms";
            resultados[i][5] = memoriaUsada + " KB";
        }

        printTable(resultados, headers);
    }
}
