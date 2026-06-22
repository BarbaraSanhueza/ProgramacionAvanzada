package com.pathfinding.app.models;

public class Edge {
    private Node destino;
    private int costo;

    public Edge(Node destino, int costo) {
        this.destino = destino;
        this.costo = costo;
    }

    public Node getDestino() {
        return destino;
    }

    public int getCosto() {
        return costo;
    }

    @Override
    public String toString() {
        return destino + "(" + costo + ")";
    }
}
