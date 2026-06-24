package org.example;

/**
 * Sistema que gestiona una fila de atención utilizando un MyDeque.
 */
class SistemaAtencion {
    private MyDeque<String> cola;

    /**
     * Constructor del SistemaAtencion.
     */
    public SistemaAtencion() {
        cola = new MyDeque<>();
    }

    /**
     * Procesa una cadena de evento y ejecuta la acción correspondiente en la fila.
     * @param eventos Cadena con la instrucción.
     */
    public void procesarEvento(String eventos) {
        if (eventos == null || eventos.trim().isEmpty()) {
            System.out.println("Error: Evento inválido o vacío.");
            return;
        }

        String[] partes = eventos.split(" ");
        String comando = partes[0];

        switch (comando) {
            case "NORMAL":
                if (partes.length > 1) {
                    cola.addLast(partes[1]);
                } else {
                    System.out.println("Error: Faltan argumentos para NORMAL");
                }
                break;

            case "PRIORITARIO":
                if (partes.length > 1) {
                    cola.addFirst(partes[1]);
                } else {
                    System.out.println("Error: Faltan argumentos para PRIORITARIO");
                }
                break;

            case "ATENDER":
                String atendido = cola.removeFirst();
                if (atendido != null) {
                    System.out.println("Atendido: " + atendido);
                }
                break;

            case "CANCELAR_ULTIMO":
                String eliminado = cola.removeLast();
                if (eliminado != null) {
                    System.out.println("Cancelado: " + eliminado);
                }
                break;

            default:
                System.out.println("Error: Comando no reconocido (" + comando + ")");
                break;
        }

        cola.mostrar();
    }
}