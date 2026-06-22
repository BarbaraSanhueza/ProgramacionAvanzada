package com.pathfinding.app.algorithms;

import com.pathfinding.app.environments.*;
import com.pathfinding.app.models.*;
import com.pathfinding.app.models.*;

import java.util.*;

public class MazeAStar {

    private static final int[] ROW_MOVES =
            {-1, 1, 0, 0};

    private static final int[] COLUMN_MOVES =
            {0, 0, -1, 1};

    public MazeSearchResult search(
            Maze maze,
            Position start,
            Position goal) {

        PriorityQueue<PositionState> openSet =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                PositionState::getCost));

        Map<Position, Integer> gScore =
                new HashMap<>();

        Map<Position, Position> parent =
                new HashMap<>();

        List<Position> visitOrder =
                new ArrayList<>();

        gScore.put(start, 0);

        openSet.add(
                new PositionState(
                        start,
                        heuristic(start, goal)));

        while (!openSet.isEmpty()) {

            PositionState state =
                    openSet.poll();

            Position current =
                    state.getPosition();

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

                int tentativeGScore =
                        gScore.get(current) + 1;

                if (!gScore.containsKey(neighbor)
                        || tentativeGScore
                        < gScore.get(neighbor)) {

                    parent.put(
                            neighbor,
                            current);

                    gScore.put(
                            neighbor,
                            tentativeGScore);

                    int fScore =
                            tentativeGScore
                                    + heuristic(
                                    neighbor,
                                    goal);

                    openSet.add(
                            new PositionState(
                                    neighbor,
                                    fScore));
                }
            }
        }

        List<Position> path =
                reconstructPath(
                        start,
                        goal,
                        parent);

        int finalCost =
                gScore.getOrDefault(
                        goal,
                        0);

        return new MazeSearchResult(
                visitOrder,
                path,
                finalCost);
    }

    private int heuristic(
            Position current,
            Position goal) {

        return Math.abs(
                current.getFila()
                        - goal.getFila())
                +
                Math.abs(
                        current.getColumna()
                                - goal.getColumna());
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