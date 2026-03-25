package org.example;

import java.util.*;

public class BenchmarkContar {

    public static void main(String[] args) {
        int[] tamanios = {10, 50, 100, 500, 1000, 5000, 10000};

        Random rand = new Random();

        for (int n : tamanios) {
            long[] tiemposLineal = new long[10];
            long[] tiemposHash = new long[10];

            for (int i = 0; i < 10; i++) {

                int[] arr = rand.ints(n, 0, 100).toArray();


                long inicio = System.nanoTime();
                Contar.conteoLineal(arr);
                long fin = System.nanoTime();
                tiemposLineal[i] = fin - inicio;

                inicio = System.nanoTime();
                Contar.conteoHash(arr);
                fin = System.nanoTime();
                tiemposHash[i] = fin - inicio;
            }

            Arrays.sort(tiemposLineal);
            Arrays.sort(tiemposHash);

            long medianaLineal = tiemposLineal[5];
            long medianaHash = tiemposHash[5];

            System.out.println("n: " + n +
                    " | Lineal: " + medianaLineal +
                    " ns | Hash: " + medianaHash + " ns");
        }
    }
}