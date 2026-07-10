package org.example;

/**
 * Representa un objeto candidato para el problema de la mochila 0/1.
 * <p>
 * Cada instancia almacena un nombre descriptivo, un peso y un valor asociado.
 * La clase funciona como modelo de datos para la solucion por programacion
 * dinamica.
 */
public class Objeto {

    private String nombre;
    private int peso;
    private int valor;

    /**
     * Crea un nuevo objeto con su nombre descriptivo, peso y valor.
     *
     * @param nombre nombre descriptivo del objeto
     * @param peso peso del objeto
     * @param valor valor del objeto
     */
    public Objeto(String nombre, int peso, int valor) {
        this.nombre = nombre;
        this.peso = peso;
        this.valor = valor;
    }

    /**
     * Obtiene el nombre descriptivo del objeto.
     *
     * @return nombre del objeto
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * Obtiene el peso del objeto.
     *
     * @return peso del objeto
     */
    public int getPeso() {
        return peso;
    }

    /**
     * Obtiene el valor del objeto.
     *
     * @return valor del objeto
     */
    public int getValor() {
        return valor;
    }
}
