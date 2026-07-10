import csv
import os
import random
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

from EmergencyCenter import EmergencyCenter
from Incident import Incident
from IncidentHashTable import IncidentHashTable
from IncidentPriorityQueue import IncidentPriorityQueue
from RoadNetwork import RoadNetwork
from RouteFinder import RouteFinder
from reportes import imprimir_reportes


Coordenada = Tuple[float, float]
COLUMNAS_CSV = ["ID", "Zona", "Latitud", "Longitud", "Prioridad", "Tipo", "Fecha"]


def generar_dataset_vial_50_nodos(network: RoadNetwork) -> List[Coordenada]:
    """Genera exactamente 50 nodos y al menos 100 aristas dirigidas. Tiempo O(V + E)."""
    random.seed(42)
    nodos: List[Coordenada] = []
    usados = set()
    while len(nodos) < 50:
        nodo = (round(random.uniform(-38.80, -38.70), 4), round(random.uniform(-72.65, -72.50), 4))
        if nodo in usados:
            continue
        usados.add(nodo)
        nodos.append(nodo)
        network.agregar_interseccion(nodo)

    for indice in range(49):
        peso = round(random.uniform(2.0, 15.0), 1)
        network.agregar_calle(nodos[indice], nodos[indice + 1], peso)

    network.agregar_calle(nodos[49], nodos[0], round(random.uniform(2.0, 15.0), 1))

    intentos = 0
    while network.cantidad_aristas() < 100 and intentos < 2000:
        origen = random.choice(nodos)
        destino = random.choice(nodos)
        if origen != destino:
            peso = round(random.uniform(3.0, 20.0), 1)
            network.agregar_calle(origen, destino, peso)
        intentos += 1
    return nodos


def csv_es_valido(ruta_csv: str) -> bool:
    """Valida cabecera y contenido minimo del CSV. Tiempo O(n), espacio O(1)."""
    if not os.path.exists(ruta_csv) or os.path.getsize(ruta_csv) == 0:
        return False
    try:
        with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != COLUMNAS_CSV:
                return False
            contador = 0
            for fila in lector:
                contador += 1
                Incident(
                    id_incidente=fila["ID"],
                    zona=fila["Zona"],
                    ubicacion=(float(fila["Latitud"]), float(fila["Longitud"])),
                    prioridad=fila["Prioridad"],
                    tipo=fila["Tipo"],
                    timestamp=fila["Fecha"],
                )
            return contador >= 500
    except (OSError, KeyError, ValueError):
        return False


def generar_csv_500_incidentes(ruta_csv: str, nodos_disponibles: List[Coordenada]) -> None:
    """Genera un CSV valido con 500 incidentes si el existente no sirve. Tiempo O(n)."""
    if csv_es_valido(ruta_csv):
        return

    random.seed(42)
    prioridades = ["Baja", "Media", "Alta", "Crítica"]
    tipos = ["Incendio", "Medico", "Rescate", "Accidente Vial", "Inundacion"]
    fecha_base = datetime(2026, 7, 1, 8, 0, 0)

    with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(COLUMNAS_CSV)
        for indice in range(1, 501):
            latitud, longitud = random.choice(nodos_disponibles)
            fecha = fecha_base + timedelta(minutes=random.randint(0, 5 * 24 * 60))
            escritor.writerow(
                [
                    f"I-{indice:03d}",
                    f"Zona_{random.randint(1, 20):02d}",
                    latitud,
                    longitud,
                    random.choice(prioridades),
                    random.choice(tipos),
                    fecha.strftime(Incident.FORMATO_FECHA),
                ]
            )


def cargar_incidentes(ruta_csv: str) -> List[Incident]:
    """Carga incidentes desde CSV validado. Tiempo O(n), espacio O(n)."""
    incidentes: List[Incident] = []
    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            incidentes.append(
                Incident(
                    id_incidente=fila["ID"],
                    zona=fila["Zona"],
                    ubicacion=(float(fila["Latitud"]), float(fila["Longitud"])),
                    prioridad=fila["Prioridad"],
                    tipo=fila["Tipo"],
                    timestamp=fila["Fecha"],
                )
            )
    return incidentes


def crear_centros(nodos: List[Coordenada]) -> List[EmergencyCenter]:
    """Crea tres centros en nodos distintos. Tiempo O(1), espacio O(1)."""
    return [
        EmergencyCenter("C-001", "Centro Norte", nodos[0]),
        EmergencyCenter("C-002", "Centro Centro", nodos[16]),
        EmergencyCenter("C-003", "Centro Sur", nodos[33]),
    ]


def seleccionar_centro_mas_cercano(
    centros: List[EmergencyCenter],
    network: RoadNetwork,
    incidente: Incident,
) -> Tuple[Optional[EmergencyCenter], Optional[dict]]:
    """
    Selecciona el centro con menor costo acumulado ejecutando Dijkstra una vez
    por centro. Ignora centros sin ruta. Tiempo O(c (V + E) log V).
    """
    mejor_centro: Optional[EmergencyCenter] = None
    mejor_resultado: Optional[dict] = None
    mejor_costo = float("inf")

    for centro in centros:
        resultado = RouteFinder.dijkstra(network, centro.ubicacion, incidente.ubicacion)
        if resultado["mensaje"] is not None or not resultado["ruta_encontrada"]:
            continue
        if resultado["costo_acumulado"] < mejor_costo:
            mejor_centro = centro
            mejor_resultado = resultado
            mejor_costo = resultado["costo_acumulado"]
    return mejor_centro, mejor_resultado


def imprimir_top_k(cola_prioridad: IncidentPriorityQueue, k: int = 10) -> None:
    """Imprime los k incidentes mas urgentes sin extraerlos. Tiempo O(k n)."""
    print("\nTop-K de incidentes criticos:")
    for posicion, incidente in enumerate(cola_prioridad.mostrar_top_k(k), start=1):
        urgencia = cola_prioridad.obtener_urgencia(incidente)
        print(f"  {posicion:02d}. {incidente.id} | {incidente.zona} | {incidente.prioridad} | urgencia={urgencia:.2f}")


def formatear_secuencia(nombre: str, valores: list, limite: int = 20) -> str:
    """Formatea secuencias largas sin saturar la consola. Tiempo O(k), espacio O(k)."""
    if len(valores) <= limite:
        return f"{nombre}: {valores}"
    muestra = valores[:limite]
    return f"{nombre}: {muestra} ... ({len(valores)} elementos en total)"


def ejecutar_escenario_integrado() -> None:
    """Ejecuta el flujo principal del proyecto integrador. Tiempo O(n log n + c (V + E) log V)."""
    try:
        mapa_vial = RoadNetwork()
        nodos_mapa = generar_dataset_vial_50_nodos(mapa_vial)
        if mapa_vial.cantidad_nodos() != 50 or mapa_vial.cantidad_aristas() < 100:
            raise RuntimeError("La red vial no cumple 50 nodos y al menos 100 aristas.")

        centros = crear_centros(nodos_mapa)
        ruta_csv = "incidentes.csv"
        generar_csv_500_incidentes(ruta_csv, nodos_mapa)
        incidentes = cargar_incidentes(ruta_csv)
        if len(incidentes) < 500:
            raise RuntimeError("El dataset tiene menos de 500 incidentes.")

        tabla_hash = IncidentHashTable(capacidad_inicial=701)
        cola_prioridad = IncidentPriorityQueue()
        for incidente in incidentes:
            tabla_hash.insertar(incidente)
            cola_prioridad.insertar(incidente)

        print("SISTEMA INTELIGENTE DE GESTION Y OPTIMIZACION DE RUTAS DE EMERGENCIA")
        print(f"Red vial: {mapa_vial.cantidad_nodos()} nodos, {mapa_vial.cantidad_aristas()} aristas dirigidas.")
        print(f"Centros cargados: {len(centros)}")
        print(f"Incidentes cargados: {len(incidentes)}")
        print("\nEstadisticas del hash:")
        for clave, valor in tabla_hash.obtener_estadisticas().items():
            print(f"  {clave}: {valor}")

        imprimir_top_k(cola_prioridad, 10)
        incidente_urgente = cola_prioridad.extraer_maximo()
        if incidente_urgente is None:
            raise RuntimeError("No hay incidentes disponibles en la cola de prioridad.")

        centro, resultado_ruta = seleccionar_centro_mas_cercano(centros, mapa_vial, incidente_urgente)

        print("\nREPORTE FINAL DE DESPACHO")
        print(f"Incidente asignado: {incidente_urgente.id}")
        print(f"Prioridad: {incidente_urgente.prioridad}")
        print(f"Zona: {incidente_urgente.zona}")
        print(f"Fecha: {incidente_urgente.timestamp}")
        print(f"Estado: {incidente_urgente.estado}")
        print(f"Tipo: {incidente_urgente.tipo}")

        if centro is None or resultado_ruta is None:
            print("No existe ningun centro con ruta disponible hacia el incidente urgente.")
        else:
            print(f"Centro asignado: {centro.id} - {centro.nombre}")
            print(formatear_secuencia("Nodos visitados completos", resultado_ruta["nodos_visitados"]))
            print(f"Cantidad de nodos visitados: {resultado_ruta['cantidad_nodos_visitados']}")
            print(formatear_secuencia("Ruta sugerida", resultado_ruta["ruta_encontrada"]))
            print(f"Cantidad de tramos: {resultado_ruta['cantidad_tramos']}")
            print(f"Distancia total: {resultado_ruta['distancia_total_aproximada']} km")
            print(f"Costo acumulado: {resultado_ruta['costo_acumulado']}")
            print(f"Tiempo estimado: {resultado_ruta['costo_acumulado']} minutos")

        imprimir_reportes(incidentes, 10)
        print("\nEjecucion finalizada con exito.")
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        print(f"Error claro del sistema: {exc}")


if __name__ == "__main__":
    ejecutar_escenario_integrado()
