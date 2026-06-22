package com.pathfinding.app.utils;

import com.pathfinding.app.models.Position;

import java.util.List;

public class MazeVisualizer {

    public static void printMaze(
            int[][] maze,
            Position start,
            Position goal,
            List<Position> path) {

        for (int fila = 0; fila < maze.length; fila++) {

            for (int columna = 0;
                 columna < maze[0].length;
                 columna++) {

                Position actual =
                        new Position(
                                fila,
                                columna);

                if (actual.equals(start)) {

                    System.out.print("S ");

                } else if (actual.equals(goal)) {

                    System.out.print("G ");

                } else if (maze[fila][columna] == 1) {

                    System.out.print("X ");

                } else if (path.contains(actual)) {

                    System.out.print("* ");

                } else {

                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
    }
}