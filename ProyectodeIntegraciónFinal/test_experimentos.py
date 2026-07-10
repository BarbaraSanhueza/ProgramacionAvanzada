import random
import time
from statistics import mean
from typing import Callable, List, Tuple

from Incident import Incident
from IncidentHashTable import IncidentHashTable
from IncidentPriorityQueue import IncidentPriorityQueue
from IncidentSorter import IncidentSorter
from RouteFinder import RouteFinder
from main import (
    cargar_incidentes,
    crear_centros,
    generar_csv_500_incidentes,
    generar_dataset_vial_50_nodos,
    seleccionar_centro_mas_cercano,
)
from RoadNetwork import RoadNetwork


def preparar_datos() -> Tuple[RoadNetwork, List[Tuple[float, float]], List[Incident]]:
    """Prepara red e incidentes fuera de las mediciones. Tiempo O(n + V + E)."""
    red = RoadNetwork()
    nodos = generar_dataset_vial_50_nodos(red)
    generar_csv_500_incidentes("incidentes.csv", nodos)
    return red, nodos, cargar_incidentes("incidentes.csv")


def experimentar_hashing(incidentes: List[Incident]) -> None:
    """Mide insercion, busqueda y operaciones basicas de hashing."""
    tabla = IncidentHashTable(capacidad_inicial=701)
    inicio = time.perf_counter()
    for incidente in incidentes:
        tabla.insertar(incidente)
    tiempo_insercion = time.perf_counter() - inicio

    ids = [incidente.id for incidente in incidentes[:500]] + [f"NO-{i:04d}" for i in range(500)]
    inicio = time.perf_counter()
    encontrados = 0
    for id_incidente in ids:
        if tabla.buscar(id_incidente) is not None:
            encontrados += 1
    tiempo_busquedas = (time.perf_counter() - inicio) / len(ids)

    id_prueba = incidentes[0].id
    ok_actualizar = tabla.actualizar_estado(id_prueba, "Asignado")
    ok_eliminar = tabla.eliminar(id_prueba)
    ok_buscar_eliminado = tabla.buscar(id_prueba) is None

    print("\nHASHING")
    print(f"Tiempo total insercion 500: {tiempo_insercion:.6f} s")
    print(f"Tiempo promedio 1000 busquedas: {tiempo_busquedas:.9f} s")
    print(f"Busquedas existentes encontradas: {encontrados}")
    print(f"Actualizar estado: {ok_actualizar} | Eliminar: {ok_eliminar} | Eliminado no encontrado: {ok_buscar_eliminado}")
    for clave, valor in tabla.obtener_estadisticas().items():
        print(f"{clave}: {valor}")


def experimentar_heap(incidentes: List[Incident]) -> None:
    """Mide operaciones del Max-Heap propio."""
    cola = IncidentPriorityQueue()
    inicio = time.perf_counter()
    for incidente in incidentes:
        cola.insertar(incidente)
    tiempo_insercion = time.perf_counter() - inicio

    esperado = cola.mostrar_top_k(1)[0]
    inicio = time.perf_counter()
    extraido = cola.extraer_maximo()
    tiempo_extraccion = time.perf_counter() - inicio

    inicio = time.perf_counter()
    actualizado = cola.actualizar_prioridad(incidentes[10].id, "Crítica")
    tiempo_actualizacion = time.perf_counter() - inicio

    inicio = time.perf_counter()
    top_k = cola.mostrar_top_k(10)
    tiempo_top_k = time.perf_counter() - inicio

    print("\nHEAP")
    print(f"Tiempo total insercion 500: {tiempo_insercion:.6f} s")
    print(f"Tiempo extraccion maximo: {tiempo_extraccion:.9f} s")
    print(f"Tiempo actualizacion prioridad: {tiempo_actualizacion:.9f} s | actualizado: {actualizado}")
    print(f"Tiempo mostrar_top_k: {tiempo_top_k:.9f} s | elementos: {len(top_k)}")
    print(f"Extraido realmente mas urgente: {extraido.id == esperado.id}")


def medir_sorter(nombre: str, funcion: Callable, datos: List[Incident], key: Callable[[Incident], object]) -> Tuple[float, float, float]:
    tiempos = []
    for _ in range(20):
        copia = list(datos)
        inicio = time.perf_counter()
        funcion(copia, key=key)
        tiempos.append(time.perf_counter() - inicio)
    return mean(tiempos), min(tiempos), max(tiempos)


def invertir_manual(lista: List[Incident]) -> List[Incident]:
    """Invierte una lista sin usar list.sort. Tiempo O(n), espacio O(n)."""
    resultado: List[Incident] = []
    for indice in range(len(lista) - 1, -1, -1):
        resultado.append(lista[indice])
    return resultado


def experimentar_sorting(incidentes: List[Incident]) -> None:
    """Compara QuickSort y MergeSort en tamanos y ordenes requeridos."""
    print("\nSORTING")
    key = lambda incidente: incidente.id
    for tamano in [100, 250, 500]:
        aleatoria = list(incidentes[:tamano])
        random.seed(42)
        random.shuffle(aleatoria)
        ordenada = IncidentSorter.mergesort(aleatoria, key=key)
        invertida = invertir_manual(ordenada)
        casos = [("aleatoria", aleatoria), ("ordenada", ordenada), ("invertida", invertida)]
        for nombre_caso, datos in casos:
            for nombre_alg, funcion in [("QuickSort", IncidentSorter.quicksort), ("MergeSort", IncidentSorter.mergesort)]:
                promedio, minimo, maximo = medir_sorter(nombre_alg, funcion, datos, key)
                print(f"N={tamano} | {nombre_caso} | {nombre_alg}: prom={promedio:.9f}s min={minimo:.9f}s max={maximo:.9f}s")


def experimentar_grafos(red: RoadNetwork, incidentes: List[Incident]) -> None:
    """Compara BFS, Dijkstra y A* bonificacion en una misma consulta."""
    centros = crear_centros(list(red.grafo.keys()))
    centro, resultado_dijkstra = seleccionar_centro_mas_cercano(centros, red, incidentes[0])
    if centro is None or resultado_dijkstra is None:
        print("\nGRAFOS: no hay ruta para el incidente de prueba.")
        return

    print("\nGRAFOS")
    for nombre, funcion in [
        ("BFS", RouteFinder.bfs),
        ("Dijkstra", RouteFinder.dijkstra),
        ("A* bonificacion", RouteFinder.a_star),
    ]:
        inicio = time.perf_counter()
        resultado = funcion(red, centro.ubicacion, incidentes[0].ubicacion)
        tiempo = time.perf_counter() - inicio
        print(f"{nombre}: tiempo={tiempo:.9f}s")
        print(f"  nodos_visitados={resultado['nodos_visitados'][:20]} total={len(resultado['nodos_visitados'])}")
        print(f"  cantidad_nodos_visitados={resultado['cantidad_nodos_visitados']}")
        print(f"  ruta={resultado['ruta_encontrada'][:20]} total={len(resultado['ruta_encontrada'])}")
        print(f"  cantidad_tramos={resultado['cantidad_tramos']}")
        print(f"  distancia={resultado['distancia_total_aproximada']} km")
        print(f"  costo_acumulado={resultado['costo_acumulado']}")


def ejecutar_experimentos() -> None:
    """Ejecuta todos los experimentos requeridos."""
    red, _, incidentes = preparar_datos()
    experimentar_hashing(incidentes)
    experimentar_heap(incidentes)
    experimentar_sorting(incidentes)
    experimentar_grafos(red, incidentes)


if __name__ == "__main__":
    ejecutar_experimentos()
