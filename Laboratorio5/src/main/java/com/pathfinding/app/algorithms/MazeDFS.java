package com.pathfinding.app.algorithms;

import com.pathfinding.app.environments.Maze;
import com.pathfinding.app.models.MazeSearchResult;
import com.pathfinding.app.models.Position;

import java.util.*;

public class MazeDFS {

    private static final int[] ROW_MOVES =
            {-1, 1, 0, 0};

    private static final int[] COLUMN_MOVES =
            {0, 0, -1, 1};

    public MazeSearchResult search(
            Maze maze,
            Position start,
            Position goal) {

        Stack<Position> stack =
                new Stack<>();

        Set<Position> visited =
                new HashSet<>();

        Map<Position, Position> parent =
                new HashMap<>();

        List<Position> visitOrder =
                new ArrayList<>();

        stack.push(start);

        while (!stack.isEmpty()) {

            Position current =
                    stack.pop();

            if (visited.contains(current)) {
                continue;
            }

            visited.add(current);

            visitOrder.add(current);

            if (current.equals(goal)) {
                break;
            }

            for (int i = 3; i >= 0; i--) {

                int newRow =
                        current.getFila()
                                + ROW_MOVES[i];

                int newColumn =
                        current.getColumna()
                                + COLUMN_MOVES[i];

                if (!maze.isValidPosition(
                        newRow,
                        newColumn)) {

                    continue;
                }

                Position neighbor =
                        new Position(
                                newRow,
                                newColumn);

                if (!visited.contains(
                        neighbor)) {

                    if (!parent.containsKey(
                            neighbor)) {

                        parent.put(
                                neighbor,
                                current);
                    }

                    stack.push(neighbor);
                }
            }
        }

        List<Position> path =
                reconstructPath(
                        start,
                        goal,
                        parent);

        int cost = path.isEmpty()
                ? 0
                : path.size() - 1;

        return new MazeSearchResult(
                visitOrder,
                path,
                cost);
    }

    private List<Position> reconstructPath(
            Position start,
            Position goal,
            Map<Position, Position> parent) {

        List<Position> path =
                new ArrayList<>();

        if (!start.equals(goal)
                && !parent.containsKey(goal)) {

            return path;
        }

        Position current = goal;

        while (current != null) {

            path.add(current);

            current = parent.get(current);
        }
        Collections.reverse(path);
        return path;
    }
}