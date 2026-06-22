package com.pathfinding.app.models;

public class PositionState {

    private Position position;
    private int cost;

    public PositionState(
            Position position,
            int cost) {

        this.position = position;
        this.cost = cost;
    }

    public Position getPosition() {
        return position;
    }

    public int getCost() {
        return cost;
    }
}
