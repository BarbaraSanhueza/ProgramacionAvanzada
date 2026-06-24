package org.example;

/**
 * Representa un nodo para una estructura de datos doblemente enlazada.
 * @param <T> Tipo de dato genérico que almacenará el nodo.
 */
class Nodo<T> {
    T dato;
    Nodo<T> siguiente;
    Nodo<T> anterior;

    /**
     * Constructor nodo.
     * @param dato El elemento a almacenar en el nodo.
     */
    public Nodo(T dato) {
        this.dato = dato;
        this.siguiente = null;
        this.anterior = null;
    }
}