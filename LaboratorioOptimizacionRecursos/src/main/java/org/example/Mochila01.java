package org.example;

import java.util.*;

/**
 * Implementa el problema de la mochila 0/1 mediante programacion dinamica.
 * <p>
 * La clase ofrece una ejecucion directa con un conjunto fijo de objetos y una
 * rutina de experimentos que evalua la misma recurrencia sobre varios tamanos
 * de entrada.
 */
public class Mochila01 {

    /**
     * Punto de entrada del programa.
     * <p>
     * Construye una instancia fija del problema, la resuelve una vez y luego
     * ejecuta la serie de experimentos.
     *
     * @param args argumentos de linea de comandos, no utilizados
     */
    public static void main(String[] args) {
        List<Objeto> objetos = new ArrayList<>();

        // Conjunto fijo de objetos usado para demostrar la solucion.
        objetos.add(new Objeto("Agua", 2, 6));
        objetos.add(new Objeto("Medicamentos", 3, 8));
        objetos.add(new Objeto("Alimentos", 4, 7));
        objetos.add(new Objeto("Radio", 5, 10));
        objetos.add(new Objeto("Generador", 9, 15));
        objetos.add(new Objeto("Herramientas", 7, 12));

        int capacidad = 20;

        resolverMochila(objetos, capacidad);

        experimento();
    }

    /**
     * Resuelve el problema de la mochila 0/1 para una lista de objetos y una
     * capacidad dada.
     * <p>
     * La tabla {@code dp[i][j]} almacena el valor maximo alcanzable usando los
     * primeros {@code i} objetos con una capacidad maxima de {@code j}.
     *
     * @param objetos lista de objetos disponibles
     * @param capacidad capacidad maxima de la mochila
     */
    public static void resolverMochila(List<Objeto> objetos, int capacidad) {
        int n = objetos.size();
        int[][] dp = new int[n + 1][capacidad + 1];

        // Inicializacion de la tabla DP: la fila 0 y la columna 0 permanecen en cero.
        for (int i = 1; i <= n; i++) {

            Objeto objetoActual = objetos.get(i - 1);

            for (int j = 1; j <= capacidad; j++) {

                if (objetoActual.getPeso() <= j) {

                    // Decide entre incluir el objeto actual o excluirlo.
                    int incluirObjeto = objetoActual.getValor()
                            + dp[i - 1][j - objetoActual.getPeso()];

                    int noIncluir = dp[i - 1][j];

                    dp[i][j] = Math.max(incluirObjeto, noIncluir);

                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        System.out.println("Valor maximo: " + dp[n][capacidad]);

        List<Objeto> seleccionados = new ArrayList<>();

        int j = capacidad;

        // Reconstruccion de la solucion optima a partir de la tabla DP.
        for (int i = n; i > 0; i--) {

            if (dp[i][j] != dp[i - 1][j]) {

                Objeto objeto = objetos.get(i - 1);
                seleccionados.add(objeto);

                j -= objeto.getPeso();
            }
        }

        System.out.println("\nObjetos seleccionados:");

        int pesoTotal = 0;
        int valorTotal = 0;

        for (Objeto obj : seleccionados) {
            System.out.println(
                    obj.getNombre() +
                            " | Peso: " + obj.getPeso() +
                            " | Valor: " + obj.getValor()
            );

            // Calculo del peso total de los objetos seleccionados.
            pesoTotal += obj.getPeso();

            // Calculo del valor total de los objetos seleccionados.
            valorTotal += obj.getValor();
        }

        System.out.println("\nPeso total: " + pesoTotal);
        System.out.println("Valor total: " + valorTotal);

        System.out.println("\nCada fila representa los primeros objetos considerados.");
        System.out.println("Cada columna representa una capacidad posible.");
        System.out.println("Cada celda contiene el valor maximo alcanzable.");
        System.out.println("\nTabla DP:");

        System.out.printf("%-16s", "Objeto/Cap.");
        for (int w = 0; w <= capacidad; w++) {
            System.out.printf("%8d", w);
        }
        System.out.println();

        System.out.printf("%-16s", "Ninguno");
        for (int w = 0; w <= capacidad; w++) {
            System.out.printf("%8d", dp[0][w]);
        }
        System.out.println();

        for (int i = 1; i <= n; i++) {
            System.out.printf("%-16s", objetos.get(i - 1).getNombre());
            for (int w = 0; w <= capacidad; w++) {
                System.out.printf("%8d", dp[i][w]);
            }
            System.out.println();
        }
    }

    /**
     * Ejecuta una serie de experimentos con cantidades crecientes de objetos.
     * <p>
     * Para cada caso, el metodo genera objetos aleatorios, resuelve el problema,
     * mide el tiempo de ejecucion e informa el tamano de la tabla dinamica.
     */
    public static void experimento() {

        int[] cantidades = {10, 20, 50, 100, 200};

        Random random = new Random();

        System.out.println("\nParte D - Experimentos");
        System.out.println("Objetos\tCapacidad\tTiempo(ns)\tTamano DP\tValor optimo");

        for (int cantidad : cantidades) {

            List<Objeto> objetos = new ArrayList<>();

            // Generacion de objetos aleatorios para este experimento.
            for (int i = 1; i <= cantidad; i++) {
                int peso = random.nextInt(20) + 1;
                int valor = random.nextInt(100) + 1;

                objetos.add(new Objeto("Objeto " + i, peso, valor));
            }

            int capacidad = cantidad * 5;

            // Medicion del tiempo de ejecucion de la solucion por DP.
            long inicio = System.nanoTime();

            int valorOptimo = calcularMochila(objetos, capacidad);

            long fin = System.nanoTime();

            long tiempo = fin - inicio;

            int filas = cantidad + 1;
            int columnas = capacidad + 1;

            // Calculo del tamano total de la tabla DP.
            int tamanoDP = filas * columnas;

            System.out.println(
                    cantidad + "\t" +
                            capacidad + "\t\t" +
                            tiempo + "\t" +
                            tamanoDP + "\t\t" +
                            valorOptimo
            );
        }
    }

    /**
     * Calcula solo el valor optimo del problema de la mochila 0/1.
     * <p>
     * Este metodo utiliza la misma recurrencia de programacion dinamica que la
     * solucion completa, pero no reconstruye los objetos seleccionados.
     *
     * @param objetos lista de objetos disponibles
     * @param capacidad capacidad maxima de la mochila
     * @return valor maximo alcanzable
     */
    public static int calcularMochila(List<Objeto> objetos, int capacidad) {

        int n = objetos.size();
        int[][] dp = new int[n + 1][capacidad + 1];

        // Inicializacion de la tabla DP: la fila 0 y la columna 0 permanecen en cero.
        for (int i = 1; i <= n; i++) {

            Objeto objetoActual = objetos.get(i - 1);

            for (int j = 1; j <= capacidad; j++) {

                if (objetoActual.getPeso() <= j) {

                    int incluir = objetoActual.getValor()
                            + dp[i - 1][j - objetoActual.getPeso()];

                    int noIncluir = dp[i - 1][j];

                    dp[i][j] = Math.max(incluir, noIncluir);

                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[n][capacidad];
    }
}
