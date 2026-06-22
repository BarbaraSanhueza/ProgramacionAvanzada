package com.pathfinding.app.environments;

public class Maze {

    private final int[][] matrix;

    public Maze() {

        matrix = new int[][]{
                {0, 0, 0, 1, 0},
                {1, 1, 0, 1, 0},
                {0, 0, 0, 0, 0},
                {0, 1, 1, 1, 0},
                {0, 0, 0, 0, 0}
        };
    }

    public int[][] getMatrix() {
        return matrix;
    }

    public int getRows() {
        return matrix.length;
    }

    public int getColumns() {
        return matrix[0].length;
    }

    public boolean isValidPosition(
            int row,
            int column) {

        return row >= 0
                && row < matrix.length
                && column >= 0
                && column < matrix[0].length
                && matrix[row][column] == 0;
    }
}