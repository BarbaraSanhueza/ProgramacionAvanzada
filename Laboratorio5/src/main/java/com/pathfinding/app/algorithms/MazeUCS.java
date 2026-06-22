package com.pathfinding.app.algorithms;

import com.pathfinding.app.environments.*;
import com.pathfinding.app.models.*;

import java.util.*;

public class MazeUCS {

    private static final int[] ROW_MOVES =
            {-1, 1, 0, 0};

    private static final int[] COLUMN_MOVES =
            {0, 0, -1, 1};

    public MazeSearchResult search(
            Maze maze,
            Position start,
            Position goal) {

        PriorityQueue<PositionState> queue =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                PositionState::getCost));

        Map<Position, Integer> costs =
                new HashMap<>();

        Map<Position, Position> parent =
                new HashMap<>();

        List<Position> visitOrder =
                new ArrayList<>();

        queue.add(
                new PositionState(
                        start,
                        0));

        costs.put(start, 0);

        while (!queue.isEmpty()) {

            PositionState state =
                    queue.poll();

            Position current =
                    state.getPosition();

            int currentCost =
                    state.getCost();

            visitOrder.add(current);

            if (current.equals(goal)) {
                break;
            }

            for (int i = 0; i < 4; i++) {

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

                int newCost =
                        currentCost + 1;

                if (!costs.containsKey(neighbor)
                        || newCost < costs.get(neighbor)) {

                    costs.put(
                            neighbor,
                            newCost);

                    parent.put(
                            neighbor,
                            current);

                    queue.add(
                            new PositionState(
                                    neighbor,
                                    newCost));
                }
            }
        }

        List<Position> path =
                reconstructPath(
                        start,
                        goal,
                        parent);

        int finalCost =
                costs.getOrDefault(
                        goal,
                        0);

        return new MazeSearchResult(
                visitOrder,
                path,
                finalCost);
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