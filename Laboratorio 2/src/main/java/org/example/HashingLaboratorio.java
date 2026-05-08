package org.example;
import java.util.*;

public class HashingLaboratorio {

    static String tipoHash = "sum";

    public static void main(String[] args) {

        int n = 1000;
        int tamanio = 211;

        runExperiment("random", generarRandom(n, 8), tamanio);

        runExperiment("secuencial", generarSecuencial(n), tamanio);

        runExperiment("agrupado", generarAgrupado(n), tamanio);
    }

    static void runExperiment(String nombre, List<String> datos, int tamanio){

        System.out.println("\nDataset: " + nombre);

        tipoHash = "sum";
        TablaHash tabla1 = new TablaHash(tamanio, 0, 0);

        long inicio1 = System.nanoTime();

        for(String k : datos){
            tabla1.inserte(k, 1);
        }

        long fin1 = System.nanoTime();

        System.out.println("\nHash Suma");
        tabla1.reporte();
        System.out.println("Tiempo: " + (fin1 - inicio1)/1_000_000.0 + " ms");

        tipoHash = "poly";
        TablaHash tabla2 = new TablaHash(tamanio, 0, 0);

        long inicio2 = System.nanoTime();

        for(String k : datos){
            tabla2.inserte(k, 1);
        }

        long fin2 = System.nanoTime();

        System.out.println("\nHash Polinomial");
        tabla2.reporte();
        System.out.println("Tiempo: " + (fin2 - inicio2)/1_000_000.0 + " ms");
    }

    // genera strings aleatorios
    static List<String> generarRandom(int n, int largo){

        Random r = new Random(42);
        List<String> lista = new ArrayList<>();
        String letras = "abcdefghijklmnopqrstuvwxyz";

        for(int i = 0; i < n; i++){
            StringBuilder sb = new StringBuilder();

            for(int j = 0; j < largo; j++){
                sb.append(letras.charAt(r.nextInt(letras.length())));
            }

            lista.add(sb.toString());
        }

        return lista;
    }

    // genera secuenciales
    static List<String> generarSecuencial(int n){

        List<String> lista = new ArrayList<>();

        for(int i = 0; i < n; i++){
            lista.add("user" + i);
        }

        return lista;
    }

    // genera agrupados
    static List<String> generarAgrupado(int n){

        List<String> lista = new ArrayList<>();

        for(int i = 0; i < n; i++){
            lista.add("aaa" + i);
        }

        return lista;
    }

    // guarda clave y valor
    static class Par{
        String clave;
        int valor;

        Par(String clave, int valor){
            this.clave = clave;
            this.valor = valor;
        }
    }

    // tabla hash
    static class TablaHash{

        private List<List<Par>> tabla;
        private int tamanio;
        private int cuenta;
        private int colisiones;

        // crea tabla
        public TablaHash(int tamanio, int cuenta, int colisiones){
            this.tamanio = tamanio;
            this.cuenta = cuenta;
            this.colisiones = colisiones;

            tabla = new ArrayList<>();
            for (int i = 0; i < tamanio; i++) {
                tabla.add(new LinkedList<>());
            }
        }

        // selecciona hash
        private int hash(String clave){
            if(tipoHash.equals("sum")){
                return HashSuma(clave);
            } else {
                return HashPolynomial(clave);
            }
        }

        // suma ascii
        private int HashSuma(String clave){
            int total = 0;

            for (int i = 0; i < clave.length(); i++) {
                total += clave.charAt(i);
            }

            return Math.floorMod(total, tamanio);
        }

        // hash polinomial
        private int HashPolynomial(String clave){

            int h = 0;

            for (int i = 0; i < clave.length(); i++) {
                h = h * 31 + clave.charAt(i);
            }

            return Math.floorMod(h, tamanio);
        }

        // inserta
        public void inserte(String clave, int valor){

            int indice = hash(clave);
            List<Par> lista = tabla.get(indice);

            for(Par p : lista){
                if(p.clave.equals(clave)){
                    p.valor = valor;
                    return;
                }
            }

            if(!lista.isEmpty()){
                colisiones++;
            }

            lista.add(new Par(clave, valor));
            cuenta++;
        }

        // busca
        public Integer buscar(String clave){

            int indice = hash(clave);

            for(Par p : tabla.get(indice)){
                if(p.clave.equals(clave)){
                    return p.valor;
                }
            }

            return null;
        }

        // elimina
        public boolean borrar(String clave){

            int indice = hash(clave);
            List<Par> lista = tabla.get(indice);

            for(int i = 0; i < lista.size(); i++){
                if(lista.get(i).clave.equals(clave)){
                    lista.remove(i);
                    cuenta--;
                    return true;
                }
            }

            return false;
        }

        // factor carga
        public double factorCarga(){
            return (double) cuenta / tamanio;
        }

        // buckets usados
        public int bucketsUsados(){

            int usados = 0;

            for(List<Par> lista : tabla){
                if(!lista.isEmpty()){
                    usados++;
                }
            }

            return usados;
        }

        // bucket maximo
        public int bucketMaximo(){

            int max = 0;

            for(List<Par> lista : tabla){
                if(lista.size() > max){
                    max = lista.size();
                }
            }

            return max;
        }

        // reporte
        public void reporte(){

            System.out.println("Tamaño tabla: " + tamanio);
            System.out.println("Elementos: " + cuenta);
            System.out.println("Factor carga: " + factorCarga());
            System.out.println("Colisiones: " + colisiones);
            System.out.println("Buckets usados: " + bucketsUsados());
            System.out.println("Bucket maximo: " + bucketMaximo());
        }
    }
}