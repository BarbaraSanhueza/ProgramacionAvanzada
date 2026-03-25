package org.example;
import java.util.HashMap;

public class Contar {

    public static HashMap<Integer, Integer> conteoLineal(int[] arr) {
        HashMap<Integer, Integer> resultado = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            int contador = 0;

            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    contador++;
                }
            }
            resultado.put(arr[i], contador);
        }
        return resultado;
    }

    public static HashMap<Integer, Integer> conteoHash(int[] arr) {
        HashMap<Integer, Integer> resultado = new HashMap<>();

        for (int num : arr) {
            if (resultado.containsKey(num)) {
                resultado.put(num, resultado.get(num) + 1);
            } else {
                resultado.put(num, 1);
            }
        }
        return resultado;
    }
}