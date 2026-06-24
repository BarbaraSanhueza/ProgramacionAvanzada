package org.example;

/**
 * Clase principal para probar el funcionamiento básico del SistemaAtencion.
 */
public class Main {
    public static void main(String[] args) {

        SistemaAtencion sistema = new SistemaAtencion();

        sistema.procesarEvento("NORMAL Matias");
        sistema.procesarEvento("NORMAL Johana");
        sistema.procesarEvento("PRIORITARIO Dolores");

        sistema.procesarEvento("NORMAL");

        sistema.procesarEvento("ATENDER");
        sistema.procesarEvento("CANCELAR_ULTIMO");
    }
}