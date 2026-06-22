package com.pathfinding.app;

import com.pathfinding.app.algorithms.*;
import com.pathfinding.app.environments.Maze;
import com.pathfinding.app.models.Graph;
import com.pathfinding.app.models.MazeSearchResult;
import com.pathfinding.app.models.Node;
import com.pathfinding.app.models.Position;
import com.pathfinding.app.models.SearchResult;
import com.pathfinding.app.utils.MazeVisualizer;

import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("SEARCH ALGORITHMS");
        System.out.println("1. Graph");
        System.out.println("2. Maze");

        int environmentOption = scanner.nextInt();

        if (environmentOption == 1) {
            executeGraphSearch();
        } else if (environmentOption == 2) {
            executeMazeSearch();
        } else {
            System.out.println("Invalid option.");
        }

        scanner.close();
    }

    private static void executeGraphSearch() {

        Graph graph = buildSampleGraph();

        System.out.println("\nAvailable nodes:");
        System.out.println("A B C D E F");

        System.out.print("Start node: ");
        String startName = scanner.next();

        System.out.print("Goal node: ");
        String goalName = scanner.next();

        Node start = findNode(graph, startName);
        Node goal = findNode(graph, goalName);

        if (start == null || goal == null) {
            System.out.println("Node not found.");
            return;
        }

        System.out.println("\nAlgorithm:");
        System.out.println("1. BFS");
        System.out.println("2. DFS");
        System.out.println("3. UCS");
        System.out.println("4. A*");

        int algorithm = scanner.nextInt();

        SearchResult result;

        switch (algorithm) {
            case 1:
                result = new GraphBFS().buscar(graph, start, goal);
                break;
            case 2:
                result = new GraphDFS().buscar(graph, start, goal);
                break;
            case 3:
                result = new GraphUCS().buscar(graph, start, goal);
                break;
            case 4:
                result = new GraphAStar().buscar(graph, start, goal);
                break;
            default:
                System.out.println("Invalid algorithm.");
                return;
        }

        System.out.println("\nVisited nodes:");
        System.out.println(result.getVisitados());

        System.out.println("\nPath:");
        System.out.println(result.getCamino());

        System.out.println("\nCost:");
        System.out.println(result.getCosto());
    }

    private static void executeMazeSearch() {

        Maze maze = new Maze();

        System.out.println("\nMaze dimensions:");
        System.out.println("Rows: " + maze.getRows());
        System.out.println("Columns: " + maze.getColumns());
        System.out.println("Use positions from 0 to rows-1 / columns-1");
        System.out.println("0 = free, 1 = wall");

        System.out.print("Start row: ");
        int startRow = scanner.nextInt();

        System.out.print("Start column: ");
        int startColumn = scanner.nextInt();

        System.out.print("Goal row: ");
        int goalRow = scanner.nextInt();

        System.out.print("Goal column: ");
        int goalColumn = scanner.nextInt();

        Position start = new Position(startRow, startColumn);
        Position goal = new Position(goalRow, goalColumn);

        if (!maze.isValidPosition(startRow, startColumn)) {
            System.out.println("Invalid start position.");
            return;
        }

        if (!maze.isValidPosition(goalRow, goalColumn)) {
            System.out.println("Invalid goal position.");
            return;
        }

        System.out.println("\nAlgorithm:");
        System.out.println("1. BFS");
        System.out.println("2. DFS");
        System.out.println("3. UCS");
        System.out.println("4. A*");

        int algorithm = scanner.nextInt();

        MazeSearchResult result;

        switch (algorithm) {
            case 1:
                result = new MazeBFS().search(maze, start, goal);
                break;
            case 2:
                result = new MazeDFS().search(maze, start, goal);
                break;
            case 3:
                result = new MazeUCS().search(maze, start, goal);
                break;
            case 4:
                result = new MazeAStar().search(maze, start, goal);
                break;
            default:
                System.out.println("Invalid algorithm.");
                return;
        }

        System.out.println("\nVisited positions:");
        System.out.println(result.getVisited());

        System.out.println("\nPath:");
        System.out.println(result.getPath());

        System.out.println("\nCost:");
        System.out.println(result.getCost());

        System.out.println("\nMaze visualization:");
        MazeVisualizer.printMaze(
                maze.getMatrix(),
                start,
                goal,
                result.getPath()
        );
    }

    private static Node findNode(Graph graph, String name) {
        for (Node node : graph.obtenerNodos()) {
            if (node.getNombre().equalsIgnoreCase(name)) {
                return node;
            }
        }
        return null;
    }

    private static Graph buildSampleGraph() {
        Graph graph = new Graph();

        Node a = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");
        Node d = new Node("D");
        Node e = new Node("E");
        Node f = new Node("F");

        graph.agregarArista(a, b, 2);
        graph.agregarArista(a, c, 4);
        graph.agregarArista(b, d, 3);
        graph.agregarArista(b, e, 5);
        graph.agregarArista(c, e, 1);
        graph.agregarArista(d, f, 4);
        graph.agregarArista(e, f, 2);

        return graph;
    }
}