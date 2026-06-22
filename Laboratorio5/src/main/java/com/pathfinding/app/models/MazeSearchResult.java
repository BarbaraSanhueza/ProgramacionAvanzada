package com.pathfinding.app.models;

import java.util.List;

public class MazeSearchResult {

    private List<Position> visited;
    private List<Position> path;
    private int cost;

    public MazeSearchResult(
            List<Position> visited,
            List<Position> path,
            int cost) {

        this.visited = visited;
        this.path = path;
        this.cost = cost;
    }

    public List<Position> getVisited() {
        return visited;
    }

    public List<Position> getPath() {
        return path;
    }

    public int getCost() {
        return cost;
    }
}
