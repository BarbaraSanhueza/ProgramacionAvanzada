package org.example;
import org.junit.jupiter.api.Test;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.*;

public class ContarTest {

    @Test
    public void testCasoNormal() {
        int[] arr = {1, 2, 2, 3, 1};

        HashMap<Integer, Integer> esperado = new HashMap<>();
        esperado.put(1, 2);
        esperado.put(2, 2);
        esperado.put(3, 1);

        assertEquals(esperado, Contar.conteoHash(arr));
        assertEquals(esperado, Contar.conteoLineal(arr));
    }

    @Test
    public void testVacio() {
        int[] arr = {};

        assertTrue(Contar.conteoHash(arr).isEmpty());
        assertTrue(Contar.conteoLineal(arr).isEmpty());
    }

    @Test
    public void testUnElemento() {
        int[] arr = {5};

        HashMap<Integer, Integer> esperado = new HashMap<>();
        esperado.put(5, 1);

        assertEquals(esperado, Contar.conteoHash(arr));
        assertEquals(esperado, Contar.conteoLineal(arr));
    }
}