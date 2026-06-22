package com.pathfinding.app.models;

public class Position {

    private int fila;
    private int columna;

    public Position(int fila, int columna) {
        this.fila = fila;
        this.columna = columna;
    }

    public int getFila() {
        return fila;
    }

    public int getColumna() {
        return columna;
    }

    @Override
    public boolean equals(Object obj) {

        if (this == obj) return true;

        if (!(obj instanceof Position))
            return false;

        Position otra = (Position) obj;

        return fila == otra.fila
                && columna == otra.columna;
    }

    @Override
    public int hashCode() {
        return 31 * fila + columna;
    }

    @Override
    public String toString() {
        return "(" + fila + "," + columna + ")";
    }
}
