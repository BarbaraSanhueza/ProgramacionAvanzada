package com.pathfinding.app.algorithms;
import com.pathfinding.app.models.*;
import java.util.*;

public class GraphDFS {

    public SearchResult buscar(
            Graph graph,
            Node inicio,
            Node objetivo) {

        Stack<Node> pila = new Stack<>();

        Set<Node> visitados = new HashSet<>();

        Map<Node, Node> padre = new HashMap<>();

        List<String> ordenVisita = new ArrayList<>();

        pila.push(inicio);

        while (!pila.isEmpty()) {

            Node actual = pila.pop();

            if (visitados.contains(actual)) {
                continue;
            }

            visitados.add(actual);

            ordenVisita.add(actual.getNombre());

            if (actual.equals(objetivo)) {
                break;
            }

            List<Edge> vecinos =
                    graph.obtenerVecinos(actual);

            for (int i = vecinos.size() - 1;
                 i >= 0;
                 i--) {

                Node vecino =
                        vecinos.get(i).getDestino();

                if (!visitados.contains(vecino)) {

                    if (!padre.containsKey(vecino)) {
                        padre.put(vecino, actual);
                    }

                    pila.push(vecino);
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