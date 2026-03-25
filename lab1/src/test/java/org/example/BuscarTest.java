package org.example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class BuscarTest {

    @Test
    void testBusquedaLinealEncontrado() {
        int[] arr = {1, 3, 5, 7, 9};
        int resultado = Buscar.busquedaLineal(arr, 5);
        assertEquals(2, resultado);
    }

    @Test
    void testBusquedaLinealNoEncontrado() {
        int[] arr = {1, 3, 5, 7, 9};
        int resultado = Buscar.busquedaLineal(arr, 4);
        assertEquals(-1, resultado);
    }

    @Test
    void testBusquedaBinariaEncontrado() {
        int[] arr = {1, 3, 5, 7, 9};
        int resultado = Buscar.busquedaBinaria(arr, 7);
        assertEquals(3, resultado);
    }

    @Test
    void testBusquedaBinariaNoEncontrado() {
        int[] arr = {1, 3, 5, 7, 9};
        int resultado = Buscar.busquedaBinaria(arr, 8);
        assertEquals(-1, resultado);
    }

}