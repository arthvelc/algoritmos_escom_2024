import java.util.Arrays;

public class CambioMonedas {
    public static int cambioMonedas(int[] monedas, int cantidad) {
        int[] dp = new int[cantidad + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int moneda : monedas) {
            for (int j = moneda; j <= cantidad; j++) {
                if (dp[j - moneda] != Integer.MAX_VALUE) {
                    dp[j] = Math.min(dp[j], dp[j - moneda] + 1);
                }
            }
        }

        return dp[cantidad] == Integer.MAX_VALUE ? -1 : dp[cantidad];
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
                System.out.print(cell + "\t\t");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[][] escenarios = {
            {11, 1, 2, 5},
            {30, 1, 2, 5, 10},
            {99, 1, 5, 10, 25, 50},
            {3, 2, 5, 10},
            {7, 2, 4}
        };

        String[][] resultados = new String[escenarios.length][5];
        String[] headers = {"Cantidad", "Monedas", "Resultado", "Tiempo", "Memoria"};

        for (int i = 0; i < escenarios.length; i++) {
            int cantidad = escenarios[i][0];
            int[] monedas = Arrays.copyOfRange(escenarios[i], 1, escenarios[i].length);

            long inicio = System.nanoTime();
            int resultado = cambioMonedas(monedas, cantidad);
            long fin = System.nanoTime();
            long tiempoTranscurrido = (fin - inicio) / 1000000; // Tiempo en ms

            long memoriaUsada = calcularMemoriaUsada();

            resultados[i][0] = String.valueOf(cantidad);
            resultados[i][1] = Arrays.toString(monedas);
            resultados[i][2] = String.valueOf(resultado);
            resultados[i][3] = tiempoTranscurrido + " ms";
            resultados[i][4] = memoriaUsada + " KB";
        }

        printTable(resultados, headers);
    }
}
