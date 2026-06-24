package org.example;

/**
 * Implementación de una cola doblemente terminada (Deque) personalizada.
 * Permite insertar y eliminar elementos tanto al inicio como al final.
 * * @param <T> Tipo de dato genérico de los elementos del Deque.
 */
class MyDeque<T> {
    private Nodo<T> inicio;
    private Nodo<T> fin;
    private int tamanio;

    /**
     * Inicializa un Deque vacío.
     */
    public MyDeque() {
        this.inicio = null;
        this.fin = null;
        this.tamanio = 0;
    }

    /**
     * Agrega un elemento al inicio del Deque.
     * @param dato Elemento a insertar.
     */
    public void addFirst(T dato) {
        Nodo<T> nuevo = new Nodo<>(dato);

        if (isEmpty()) {
            inicio = fin = nuevo;
        } else {
            nuevo.siguiente = inicio;
            inicio.anterior = nuevo;
            inicio = nuevo;
        }
        tamanio++;
    }

    /**
     * Agrega un elemento al final del Deque.
     * @param dato Elemento a insertar.
     */
    public void addLast(T dato) {
        Nodo<T> nuevo = new Nodo<>(dato);

        if (isEmpty()) {
            inicio = fin = nuevo;
        } else {
            fin.siguiente = nuevo;
            nuevo.anterior = fin;
            fin = nuevo;
        }
        tamanio++;
    }

    /**
     * Remueve y retorna el primer elemento del Deque.
     * @return El elemento removido o null si el Deque está vacío.
     */
    public T removeFirst() {
        if (isEmpty()) {
            System.out.println("Deque esta vacio");
            return null;
        }

        T dato = inicio.dato;

        if (inicio == fin) {
            inicio = fin = null;
        } else {
            inicio = inicio.siguiente;
            inicio.anterior = null;
        }
        tamanio--;
        return dato;
    }

    /**
     * Remueve y retorna el último elemento del Deque.
     * @return El elemento removido o null si el Deque está vacío.
     */
    public T removeLast() {
        if (isEmpty() || fin == null) {
            System.out.println("Deque vacío");
            return null;
        }

        T dato = fin.dato;

        if (inicio == fin) {
            inicio = fin = null;
        } else {
            fin = fin.anterior;
            if (fin != null) {
                fin.siguiente = null;
            }
        }

        tamanio--;
        return dato;
    }

    /**
     * Verifica si el Deque está vacío.
     * @return true si está vacío, false en caso contrario.
     */
    public boolean isEmpty() {
        return tamanio == 0;
    }

    /**
     * Obtiene el primer elemento sin removerlo.
     * @return El primer elemento o null si está vacío.
     */
    public T peekFirst() {
        return isEmpty() ? null : inicio.dato;
    }

    /**
     * Obtiene el último elemento sin removerlo.
     * @return El último elemento o null si está vacío.
     */
    public T peekLast() {
        return isEmpty() ? null : fin.dato;
    }

    /**
     * Obtiene la cantidad de elementos en el Deque.
     * @return El tamaño actual.
     */
    public int tamanio() {
        return tamanio;
    }

    /**
     * Imprime por consola el estado actual del Deque desde el inicio al fin.
     */
    public void mostrar() {
        Nodo<T> actual = inicio;
        while (actual != null) {
            System.out.print(actual.dato + " --> ");
            actual = actual.siguiente;
        }
        System.out.println("null");
    }
}