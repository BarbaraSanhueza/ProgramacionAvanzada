package com.pathfinding.app.models;

import java.util.*;

public class Graph {
    private Map<Node, List<Edge>> adyacencias;

    public Graph() {
        adyacencias = new HashMap<>();
    }

    public void agregarNodo(Node nodo) {
        adyacencias.putIfAbsent(nodo, new ArrayList<>());
    }

    public void agregarArista(Node origen,
                              Node destino,
                              int costo) {

        agregarNodo(origen);
        agregarNodo(destino);

        adyacencias.get(origen)
                .add(new Edge(destino, costo));
    }

    public List<Edge> obtenerVecinos(Node node) {
        return adyacencias.getOrDefault(
                node,
                new ArrayList<>()
        );
    }

    public Set<Node> obtenerNodos() {
        return adyacencias.keySet();
    }
}
