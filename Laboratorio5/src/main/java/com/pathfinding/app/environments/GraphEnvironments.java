package com.pathfinding.app.environments;

import com.pathfinding.app.models.Edge;
import com.pathfinding.app.models.Node;

import java.util.*;

public class GraphEnvironments {

    private Map<Node, List<Edge>> adjacencyList;

    public GraphEnvironments() {
        adjacencyList = new HashMap<>();
    }

    public void addNode(Node node) {
        adjacencyList.putIfAbsent(
                node,
                new ArrayList<>()
        );
    }

    public void addEdge(
            Node source,
            Node destination,
            int cost) {

        addNode(source);
        addNode(destination);

        adjacencyList
                .get(source)
                .add(
                        new Edge(
                                destination,
                                cost));
    }

    public List<Edge> getNeighbors(
            Node node) {

        return adjacencyList.getOrDefault(
                node,
                new ArrayList<>()
        );
    }

    public Set<Node> getNodes() {
        return adjacencyList.keySet();
    }

    public void printGraph() {

        for (Node node : adjacencyList.keySet()) {

            System.out.print(
                    node.getNombre() + " -> ");

            for (Edge edge :
                    adjacencyList.get(node)) {

                System.out.print(
                        edge.getDestino()
                                .getNombre()
                                + "("
                                + edge.getCosto()
                                + ") ");
            }

            System.out.println();
        }
    }

    public static GraphEnvironments createSampleGraph() {

        GraphEnvironments graph = new GraphEnvironments();

        Node a = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");
        Node d = new Node("D");
        Node e = new Node("E");
        Node f = new Node("F");

        graph.addEdge(a, b, 2);
        graph.addEdge(a, c, 4);

        graph.addEdge(b, d, 3);
        graph.addEdge(b, e, 5);

        graph.addEdge(c, e, 1);

        graph.addEdge(d, f, 4);

        graph.addEdge(e, f, 2);

        return graph;
    }
}