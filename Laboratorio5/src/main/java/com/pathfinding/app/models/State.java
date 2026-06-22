package com.pathfinding.app.models;

public class State {
    private Node node;
    private int costo;

    public State(Node node, int costo) {
        this.node = node;
        this.costo = costo;
    }
    public Node getNode() {
        return node;
    }

    public int getCosto() {
        return costo;
    }
}
