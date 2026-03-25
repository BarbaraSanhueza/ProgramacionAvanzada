package org.example;

public class Buscar {

    // BUsqueda lineal
    public static int busquedaLineal(int[] arreglo, int n) {
        for (int i = 0; i < arreglo.length; i++) {
            if (arreglo[i] == n) {
                return i;
            }
        }
        return -1;
    }


    // Busqueda binaria
    public static int busquedaBinaria(int[] arreglo, int n) {
        int izquierda = 0;
        int derecha = arreglo.length - 1;
        while (izquierda <= derecha) {
            int mitad = (izquierda + derecha) / 2;
            if (arreglo[mitad] == n) return mitad;
            if (arreglo[mitad] < n) {
                izquierda = mitad + 1;
            } else {
                derecha = mitad - 1;
            }
        }
        return -1;
    }
}

