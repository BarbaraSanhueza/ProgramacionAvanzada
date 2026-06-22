package com.pathfinding.app.algorithms;
import java.util.*;
import com.pathfinding.app.models.*;


public class GraphUCS {

    public SearchResult buscar(
            Graph graph,
            Node inicio,
            Node objetivo) {

        PriorityQueue<State> cola =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                State::getCosto));

        Map<Node, Integer> costos =
                new HashMap<>();

        Map<Node, Node> padre =
                new HashMap<>();

        List<String> ordenVisita =
                new ArrayList<>();

        cola.add(new State(inicio, 0));

        costos.put(inicio, 0);

        while (!cola.isEmpty()) {

            State estado = cola.poll();

            Node actual = estado.getNode();

            int costoActual =
                    estado.getCosto();

            ordenVisita.add(
                    actual.getNombre());

            if (actual.equals(objetivo)) {
                break;
            }

            for (Edge arista :
                    graph.obtenerVecinos(actual)) {

                Node vecino =
                        arista.getDestino();

                int nuevoCosto =
                        costoActual
                                + arista.getCosto();

                if (!costos.containsKey(vecino)
                        || nuevoCosto
                        < costos.get(vecino)) {

                    costos.put(
                            vecino,
                            nuevoCosto);

                    padre.put(
                            vecino,
                            actual);

                    cola.add(
                            new State(
                                    vecino,
                                    nuevoCosto));
                }
            }
        }

        List<String> camino =
                reconstruirCamino(
                        inicio,
                        objetivo,
                        padre);

        int costoFinal =
                costos.getOrDefault(
                        objetivo,
                        0);

        return new SearchResult(
                ordenVisita,
                camino,
                costoFinal);
    }

    private List<String> reconstruirCamino(
            Node inicio,
            Node objetivo,
            Map<Node, Node> padre) {

        List<String> camino =
                new ArrayList<>();

        if (!inicio.equals(objetivo)
                && !padre.containsKey(
                objetivo)) {

            return camino;
        }

        Node actual = objetivo;

        while (actual != null) {

            camino.add(
                    actual.getNombre());

            actual =
                    padre.get(actual);
        }

        Collections.reverse(camino);

        return camino;
    }
}