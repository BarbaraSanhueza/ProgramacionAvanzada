package com.pathfinding.app.models;

import java.util.List;

public class SearchResult {
    private List<String> visitados;
    private List<String> camino;
    private int costo;

    public SearchResult(
            List<String> visitados,
            List<String> camino,
            int costo) {

        this.visitados = visitados;
        this.camino = camino;
        this.costo = costo;
    }

    public List<String> getVisitados() {
        return visitados;
    }

    public List<String> getCamino() {
        return camino;
    }

    public int getCosto() {
        return costo;
    }
}
