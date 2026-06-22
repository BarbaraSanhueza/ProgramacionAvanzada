package com.pathfinding.app.algorithms;
import com.pathfinding.app.models.*;
import java.util.*;

public class GraphBFS {

    public SearchResult buscar(
            Graph graph,
            Node inicio,
            Node objetivo) {

        Queue<Node> cola = new LinkedList<>();

        Set<Node> visitados = new HashSet<>();

        Map<Node, Node> padre = new HashMap<>();

        List<String> ordenVisita = new ArrayList<>();

        cola.add(inicio);
        visitados.add(inicio);

        while (!cola.isEmpty()) {

            Node actual = cola.poll();

            ordenVisita.add(actual.getNombre());

            if (actual.equals(objetivo)) {
                break;
            }

            for (Edge arista : graph.obtenerVecinos(actual)) {

                Node vecino = arista.getDestino();

                if (!visitados.contains(vecino)) {

                    visitados.add(vecino);

                    padre.put(vecino, actual);

                    cola.add(vecino);
                }
            }
        }

        List<String> camino =
                reconstruirCamino(
                        inicio,
                        objetivo,
                        padre);

        return new SearchResult(
                ordenVisita,
                camino,
                camino.size() - 1
        );
    }

    private List<String> reconstruirCamino(
            Node inicio,
            Node objetivo,
            Map<Node, Node> padre) {

        List<String> camino = new ArrayList<>();

        if (!inicio.equals(objetivo)
                && !padre.containsKey(objetivo)) {

            return camino;
        }

        Node actual = objetivo;

        while (actual != null) {

            camino.add(actual.getNombre());

            actual = padre.get(actual);
        }

        Collections.reverse(camino);

        return camino;
    }
}