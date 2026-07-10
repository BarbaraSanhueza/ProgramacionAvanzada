from collections import deque
import heapq
import math
from typing import Any, Dict, List, Optional, Set, Tuple


Coordenada = Tuple[float, float]


class RouteFinder:
    """Algoritmos de busqueda de rutas sobre RoadNetwork."""

    @staticmethod
    def bfs(network: Any, origen: Coordenada, destino: Coordenada) -> Dict[str, Any]:
        """
        Descripcion:
            Busca una ruta por BFS ignorando pesos durante la exploracion.

        Parametros:
            network (Any): red vial con grafo y obtener_vecinos.
            origen (Coordenada): nodo inicial.
            destino (Coordenada): nodo final.

        Retorna:
            Dict[str, Any]: resultado con algoritmo, visitados, ruta, distancia y costo.

        Precondiciones:
            - origen y destino deben ser coordenadas.

        Postcondiciones:
            - No modifica la red vial.

        Excepciones:
            - Ninguna: los casos invalidos se reportan en el resultado.

        Complejidad temporal:
            O(V + E)

        Complejidad espacial:
            O(V)
        """
        validacion = RouteFinder._validar_consulta(network, origen, destino, "BFS")
        if validacion is not None:
            return validacion
        if origen == destino:
            return RouteFinder._resultado("BFS", [origen], [origen], network, 0.0, None)

        cola = deque([origen])
        visitados: Set[Coordenada] = {origen}
        padres: Dict[Coordenada, Coordenada] = {}
        orden_visitados: List[Coordenada] = []

        while cola:
            actual = cola.popleft()
            orden_visitados.append(actual)
            if actual == destino:
                break
            for vecino, _ in network.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        if destino not in visitados:
            return RouteFinder._resultado("BFS", orden_visitados, [], network, 0.0, "Destino inalcanzable.")
        ruta = RouteFinder._reconstruir_ruta(padres, origen, destino)
        costo = RouteFinder._calcular_costo_ruta(network, ruta)
        return RouteFinder._resultado("BFS", orden_visitados, ruta, network, costo, None)

    @staticmethod
    def dijkstra(network: Any, origen: Coordenada, destino: Coordenada) -> Dict[str, Any]:
        """
        Descripcion:
            Busca la ruta de menor costo acumulado con Dijkstra/UCS.

        Parametros:
            network (Any): red vial con pesos positivos.
            origen (Coordenada): nodo inicial.
            destino (Coordenada): nodo final.

        Retorna:
            Dict[str, Any]: resultado con algoritmo, visitados, ruta, distancia y costo.

        Precondiciones:
            - Los pesos del grafo deben ser positivos.

        Postcondiciones:
            - No modifica la red vial.

        Excepciones:
            - Ninguna: los casos invalidos se reportan en el resultado.

        Complejidad temporal:
            O((V + E) log V)

        Complejidad espacial:
            O(V + E)
        """
        validacion = RouteFinder._validar_consulta(network, origen, destino, "Dijkstra / UCS")
        if validacion is not None:
            return validacion
        if origen == destino:
            return RouteFinder._resultado("Dijkstra / UCS", [origen], [origen], network, 0.0, None)

        cola_prioridad: List[Tuple[float, Coordenada]] = [(0.0, origen)]
        costos: Dict[Coordenada, float] = {origen: 0.0}
        padres: Dict[Coordenada, Coordenada] = {}
        visitados: Set[Coordenada] = set()
        orden_visitados: List[Coordenada] = []

        while cola_prioridad:
            costo_actual, actual = heapq.heappop(cola_prioridad)
            if actual in visitados:
                continue
            visitados.add(actual)
            orden_visitados.append(actual)
            if actual == destino:
                break
            for vecino, peso in network.obtener_vecinos(actual):
                nuevo_costo = costo_actual + peso
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = actual
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino))

        if destino not in costos:
            return RouteFinder._resultado("Dijkstra / UCS", orden_visitados, [], network, 0.0, "Destino inalcanzable.")
        ruta = RouteFinder._reconstruir_ruta(padres, origen, destino)
        return RouteFinder._resultado("Dijkstra / UCS", orden_visitados, ruta, network, costos[destino], None)

    @staticmethod
    def a_star(network: Any, origen: Coordenada, destino: Coordenada) -> Dict[str, Any]:
        """
        Descripcion:
            Busca una ruta con A*. Usa heuristica cero para garantizar admisibilidad
            cuando los pesos representan tiempo y no distancia geografica.

        Parametros:
            network (Any): red vial.
            origen (Coordenada): nodo inicial.
            destino (Coordenada): nodo final.

        Retorna:
            Dict[str, Any]: resultado con la misma estructura de BFS y Dijkstra.

        Precondiciones:
            - Los pesos deben ser positivos.

        Postcondiciones:
            - No modifica la red vial.

        Excepciones:
            - Ninguna: los casos invalidos se reportan en el resultado.

        Complejidad temporal:
            O((V + E) log V)

        Complejidad espacial:
            O(V + E)
        """
        validacion = RouteFinder._validar_consulta(network, origen, destino, "A* (bonificacion)")
        if validacion is not None:
            return validacion
        if origen == destino:
            return RouteFinder._resultado("A* (bonificacion)", [origen], [origen], network, 0.0, None)

        cola: List[Tuple[float, float, Coordenada]] = [(0.0, 0.0, origen)]
        costos: Dict[Coordenada, float] = {origen: 0.0}
        padres: Dict[Coordenada, Coordenada] = {}
        visitados: Set[Coordenada] = set()
        orden_visitados: List[Coordenada] = []

        while cola:
            _, costo_actual, actual = heapq.heappop(cola)
            if actual in visitados:
                continue
            visitados.add(actual)
            orden_visitados.append(actual)
            if actual == destino:
                break
            for vecino, peso in network.obtener_vecinos(actual):
                nuevo_costo = costo_actual + peso
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = actual
                    heuristica_segura = 0.0
                    heapq.heappush(cola, (nuevo_costo + heuristica_segura, nuevo_costo, vecino))

        if destino not in costos:
            return RouteFinder._resultado("A* (bonificacion)", orden_visitados, [], network, 0.0, "Destino inalcanzable.")
        ruta = RouteFinder._reconstruir_ruta(padres, origen, destino)
        return RouteFinder._resultado("A* (bonificacion)", orden_visitados, ruta, network, costos[destino], None)

    @staticmethod
    def haversine(origen: Coordenada, destino: Coordenada) -> float:
        """Calcula distancia geografica aproximada en kilometros. Tiempo O(1), espacio O(1)."""
        radio_tierra_km = 6371.0
        lat1, lon1 = math.radians(origen[0]), math.radians(origen[1])
        lat2, lon2 = math.radians(destino[0]), math.radians(destino[1])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        return 2 * radio_tierra_km * math.asin(math.sqrt(a))

    @staticmethod
    def _validar_consulta(network: Any, origen: Coordenada, destino: Coordenada, algoritmo: str) -> Optional[Dict[str, Any]]:
        if origen not in network.grafo:
            return RouteFinder._resultado(algoritmo, [], [], network, 0.0, "Origen inexistente.")
        if destino not in network.grafo:
            return RouteFinder._resultado(algoritmo, [], [], network, 0.0, "Destino inexistente.")
        return None

    @staticmethod
    def _resultado(
        algoritmo: str,
        visitados: List[Coordenada],
        ruta: List[Coordenada],
        network: Any,
        costo: float,
        mensaje: Optional[str],
    ) -> Dict[str, Any]:
        distancia = RouteFinder._calcular_distancia_ruta(ruta) if ruta else 0.0
        resultado = {
            "algoritmo": algoritmo,
            "nodos_visitados": visitados,
            "cantidad_nodos_visitados": len(visitados),
            "ruta_encontrada": ruta,
            "cantidad_tramos": max(0, len(ruta) - 1),
            "distancia_total_aproximada": round(distancia, 3),
            "costo_acumulado": round(costo, 3),
            "mensaje": mensaje,
        }
        resultado["Algoritmo"] = resultado["algoritmo"]
        resultado["Nodos visitados"] = resultado["nodos_visitados"]
        resultado["Ruta encontrada"] = resultado["ruta_encontrada"]
        resultado["Costo acumulado (Tiempo total)"] = resultado["costo_acumulado"]
        return resultado

    @staticmethod
    def _reconstruir_ruta(padres: Dict[Coordenada, Coordenada], origen: Coordenada, destino: Coordenada) -> List[Coordenada]:
        ruta = [destino]
        actual = destino
        while actual != origen:
            actual = padres[actual]
            ruta.append(actual)
        ruta.reverse()
        return ruta

    @staticmethod
    def _calcular_costo_ruta(network: Any, ruta: List[Coordenada]) -> float:
        costo = 0.0
        for indice in range(len(ruta) - 1):
            origen = ruta[indice]
            destino = ruta[indice + 1]
            for vecino, peso in network.obtener_vecinos(origen):
                if vecino == destino:
                    costo += peso
                    break
        return costo

    @staticmethod
    def _calcular_distancia_ruta(ruta: List[Coordenada]) -> float:
        distancia = 0.0
        for indice in range(len(ruta) - 1):
            distancia += RouteFinder.haversine(ruta[indice], ruta[indice + 1])
        return distancia
