import csv
import time
from typing import Callable, List

from Incident import Incident
from IncidentSorter import IncidentSorter
from main import generar_csv_500_incidentes, generar_dataset_vial_50_nodos
from RoadNetwork import RoadNetwork


def cargar_incidentes_para_pruebas(ruta_csv: str) -> List[Incident]:
    """Carga incidentes desde CSV para validar sorting. Tiempo O(n), espacio O(n)."""
    red = RoadNetwork()
    nodos = generar_dataset_vial_50_nodos(red)
    generar_csv_500_incidentes(ruta_csv, nodos)
    lista: List[Incident] = []
    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista.append(
                Incident(
                    id_incidente=fila["ID"],
                    zona=fila["Zona"],
                    ubicacion=(float(fila["Latitud"]), float(fila["Longitud"])),
                    prioridad=fila["Prioridad"],
                    tipo=fila["Tipo"],
                    timestamp=fila["Fecha"],
                )
            )
    return lista


def validar_resultado(resultado: List[Incident], key: Callable[[Incident], object]) -> bool:
    """Valida contra sorted solo para pruebas. Tiempo O(n log n), espacio O(n)."""
    return resultado == sorted(resultado, key=key)


def ejecutar_experimento_sorting() -> None:
    """Ejecuta una prueba simple de QuickSort y MergeSort. Tiempo O(n log n)."""
    print("EXPERIMENTACION BASICA DE ORDENAMIENTO")
    incidentes_base = cargar_incidentes_para_pruebas("incidentes.csv")
    if not incidentes_base:
        print("No hay incidentes para probar.")
        return

    criterio = lambda incidente: incidente.id

    inicio_qk = time.perf_counter()
    resultado_qk = IncidentSorter.quicksort(list(incidentes_base), key=criterio)
    tiempo_qk = time.perf_counter() - inicio_qk

    inicio_ms = time.perf_counter()
    resultado_ms = IncidentSorter.mergesort(list(incidentes_base), key=criterio)
    tiempo_ms = time.perf_counter() - inicio_ms

    print(f"Dataset: {len(incidentes_base)} incidentes")
    print(f"QuickSort: {tiempo_qk:.6f} s | correcto: {validar_resultado(resultado_qk, criterio)}")
    print(f"MergeSort: {tiempo_ms:.6f} s | correcto: {validar_resultado(resultado_ms, criterio)}")


if __name__ == "__main__":
    ejecutar_experimento_sorting()
