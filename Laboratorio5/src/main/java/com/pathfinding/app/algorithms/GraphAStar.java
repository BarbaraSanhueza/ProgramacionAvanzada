package com.pathfinding.app.algorithms;

import com.pathfinding.app.models.*;

import java.util.*;

public class GraphAStar {


    public SearchResult buscar(
            Graph graph,
            Node inicio,
            Node objetivo) {


        PriorityQueue<State> abiertos =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                State::getCosto));


        Map<Node, Integer> gScore =
                new HashMap<>();


        Map<Node, Node> padre =
                new HashMap<>();


        List<String> ordenVisita =
                new ArrayList<>();


        gScore.put(inicio, 0);


        abiertos.add(
                new State(
                        inicio,
                        heuristica(inicio, objetivo)
                )
        );


        while (!abiertos.isEmpty()) {


            State estado =
                    abiertos.poll();


            Node actual =
                    estado.getNode();


            ordenVisita.add(
                    actual.getNombre()
            );


            if (actual.equals(objetivo)) {
                break;
            }


            for (Edge arista :
                    graph.obtenerVecinos(actual)) {


                Node vecino =
                        arista.getDestino();


                int costoTentativo =
                        gScore.get(actual)
                                + arista.getCosto();


                if (!gScore.containsKey(vecino)
                        || costoTentativo < gScore.get(vecino)) {


                    padre.put(
                            vecino,
                            actual
                    );


                    gScore.put(
                            vecino,
                            costoTentativo
                    );


                    int fScore =
                            costoTentativo
                                    + heuristica(
                                    vecino,
                                    objetivo
                            );


                    abiertos.add(
                            new State(
                                    vecino,
                                    fScore
                            )
                    );
                }
            }
        }


        List<String> camino =
                reconstruirCamino(
                        inicio,
                        objetivo,
                        padre
                );


        int costoFinal =
                gScore.getOrDefault(
                        objetivo,
                        0
                );


        return new SearchResult(
                ordenVisita,
                camino,
                costoFinal
        );
    }


    private int heuristica(
            Node actual,
            Node objetivo) {


        String nodo =
                actual.getNombre();


        String meta =
                objetivo.getNombre();


        if (nodo.equals(meta)) {
            return 0;
        }


        switch (nodo) {


            case "A":
                return 3;


            case "B":
                return 2;


            case "C":
                return 2;


            case "D":
                return 1;


            case "E":
                return 1;


            case "F":
                return 0;


            default:
                return 0;
        }
    }


    private List<String> reconstruirCamino(
            Node inicio,
            Node objetivo,
            Map<Node, Node> padre) {


        List<String> camino =
                new ArrayList<>();


        if (!inicio.equals(objetivo)
                && !padre.containsKey(objetivo)) {

            return camino;
        }


        Node actual = objetivo;


        while (actual != null) {


            camino.add(
                    actual.getNombre()
            );


            actual =
                    padre.get(actual);
        }
        Collections.reverse(camino);
        return camino;
    }
}