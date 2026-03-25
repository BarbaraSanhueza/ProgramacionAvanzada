import java.util.Arrays;
import java.util.Random;

public class BenchmarkBuscar {
    public static void main(String[] args) {

        int[] tamanios = {10, 50, 100, 500, 1000, 5000, 10000};

        Random rand = new Random();

        for (int n : tamanios) {
            long[] tiemposLineal = new long[10];
            long[] tiemposBinaria = new long[10];

            for (int i = 0; i < 10; i++) {
                int[] arr = rand.ints(n, 0, n).toArray();
                int objetivo = arr[n / 2];

                int[] arrOrdenado = Arrays.copyOf(arr, arr.length);
                Arrays.sort(arrOrdenado);

                long inicio = System.nanoTime();
                Buscar.busquedaLineal(arr, objetivo);
                long fin = System.nanoTime();
                tiemposLineal[i] = fin - inicio;

                inicio = System.nanoTime();
                Buscar.busquedaBinaria(arrOrdenado, objetivo);
                fin = System.nanoTime();
                tiemposBinaria[i] = fin - inicio;
            }
            Arrays.sort(tiemposLineal);
            Arrays.sort(tiemposBinaria);

            long medianaLineal = tiemposLineal[5];
            long medianaBinaria = tiemposBinaria[5];
            System.out.println("n=" + n +
                    " | Lineal: " + medianaLineal +
                    " ns | Binaria: " + medianaBinaria + " ns");
        }
    }
}
