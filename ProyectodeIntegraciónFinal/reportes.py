from typing import Dict, List, Tuple

from Incident import Incident
from IncidentPriorityQueue import IncidentPriorityQueue
from IncidentSorter import IncidentSorter


def incidentes_mas_antiguos(incidentes: List[Incident], limite: int = 10) -> List[Incident]:
    """
    Descripcion:
        Genera un reporte de incidentes por fecha ascendente.

    Parametros:
        incidentes (List[Incident]): incidentes a ordenar.
        limite (int): cantidad maxima de resultados.

    Retorna:
        List[Incident]: primeros incidentes mas antiguos.

    Precondiciones:
        - incidentes debe contener timestamps validos.

    Postcondiciones:
        - No modifica la lista original.

    Excepciones:
        - ValueError: si limite es negativo.

    Complejidad temporal:
        O(n log n)

    Complejidad espacial:
        O(n)
    """
    if limite < 0:
        raise ValueError("limite debe ser no negativo.")
    ordenados = IncidentSorter.mergesort(incidentes, key=lambda inc: inc.fecha_datetime())
    return ordenados[:limite]


def incidentes_mas_criticos(incidentes: List[Incident], limite: int = 10) -> List[Incident]:
    """
    Descripcion:
        Genera un reporte de incidentes por urgencia descendente.

    Parametros:
        incidentes (List[Incident]): incidentes a ordenar.
        limite (int): cantidad maxima de resultados.

    Retorna:
        List[Incident]: incidentes mas urgentes.

    Precondiciones:
        - incidentes debe contener prioridad y timestamp validos.

    Postcondiciones:
        - No modifica la lista original.

    Excepciones:
        - ValueError: si limite es negativo.

    Complejidad temporal:
        O(n log n)

    Complejidad espacial:
        O(n)
    """
    if limite < 0:
        raise ValueError("limite debe ser no negativo.")
    cola = IncidentPriorityQueue()
    ordenados = IncidentSorter.mergesort(incidentes, key=lambda inc: -cola.obtener_urgencia(inc))
    return ordenados[:limite]


def zonas_con_mas_incidentes(incidentes: List[Incident], limite: int = 10) -> List[Tuple[str, int]]:
    """
    Descripcion:
        Genera un reporte de zonas ordenadas por cantidad descendente.

    Parametros:
        incidentes (List[Incident]): incidentes a agrupar.
        limite (int): cantidad maxima de zonas.

    Retorna:
        List[Tuple[str, int]]: pares (zona, cantidad).

    Precondiciones:
        - cada incidente debe tener zona valida.

    Postcondiciones:
        - No modifica los incidentes.

    Excepciones:
        - ValueError: si limite es negativo.

    Complejidad temporal:
        O(n + z log z), donde z es la cantidad de zonas.

    Complejidad espacial:
        O(z)
    """
    if limite < 0:
        raise ValueError("limite debe ser no negativo.")
    conteos: Dict[str, int] = {}
    for incidente in incidentes:
        conteos[incidente.zona] = conteos.get(incidente.zona, 0) + 1
    pares = [(zona, cantidad) for zona, cantidad in conteos.items()]
    ordenados = IncidentSorter.mergesort(pares, key=lambda par: (-par[1], par[0]))
    return ordenados[:limite]


def imprimir_reportes(incidentes: List[Incident], limite: int = 10) -> None:
    """Imprime los tres reportes requeridos. Tiempo O(n log n), espacio O(n)."""
    print("\nREPORTES ORDENADOS")
    print("Incidentes mas antiguos:")
    for inc in incidentes_mas_antiguos(incidentes, limite):
        print(f"  {inc.id} | {inc.zona} | {inc.timestamp} | {inc.prioridad} | {inc.tipo}")

    print("\nIncidentes mas criticos:")
    cola = IncidentPriorityQueue()
    for inc in incidentes_mas_criticos(incidentes, limite):
        print(f"  {inc.id} | urgencia={cola.obtener_urgencia(inc):.2f} | {inc.zona} | {inc.prioridad} | {inc.timestamp}")

    print("\nZonas con mas incidentes:")
    for zona, cantidad in zonas_con_mas_incidentes(incidentes, limite):
        print(f"  {zona}: {cantidad}")
