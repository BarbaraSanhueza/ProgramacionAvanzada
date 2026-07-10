import json
from typing import Dict, List, Tuple


Coordenada = Tuple[float, float]


class RoadNetwork:
    """
    ADT RoadNetwork.

    Proposito:
        Representar una red vial dirigida y ponderada para planificar rutas
        de emergencia.

    Representacion interna:
        Grafo dirigido mediante lista de adyacencia:
        dict[coordenada_origen] -> list[(coordenada_destino, peso)].

    Atributos:
        grafo (Dict[Coordenada, List[Tuple[Coordenada, float]]]): lista de
        adyacencia con pesos positivos.

    Invariantes:
        - Todo nodo origen existe como clave en grafo.
        - Toda arista apunta a un nodo existente.
        - Todo peso es positivo.
        - No hay aristas duplicadas con el mismo origen y destino.

    Responsabilidades:
        - Mantener intersecciones y calles dirigidas.
        - Validar nodos y pesos.
        - Exponer metricas basicas del grafo.
        - Cargar una red desde JSON.
    """

    def __init__(self) -> None:
        """
        Descripcion:
            Inicializa una red vial vacia.

        Parametros:
            Ninguno.

        Retorna:
            None: el constructor no retorna valor.

        Precondiciones:
            - Ninguna.

        Postcondiciones:
            - grafo queda inicializado sin nodos ni aristas.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self.grafo: Dict[Coordenada, List[Tuple[Coordenada, float]]] = {}

    @staticmethod
    def _validar_coordenada(coordenada: Coordenada) -> None:
        if not isinstance(coordenada, tuple) or len(coordenada) != 2:
            raise ValueError("La coordenada debe ser una tupla (latitud, longitud).")
        latitud, longitud = coordenada
        if not isinstance(latitud, (int, float)) or not isinstance(longitud, (int, float)):
            raise ValueError("La coordenada debe contener valores numericos.")

    def agregar_interseccion(self, coordenada: Coordenada) -> None:
        """
        Descripcion:
            Agrega una interseccion si no existe.

        Parametros:
            coordenada (Coordenada): nodo representado por latitud y longitud.

        Retorna:
            None: modifica el grafo en sitio.

        Precondiciones:
            - coordenada debe contener dos numeros.

        Postcondiciones:
            - La coordenada existe como nodo del grafo.

        Excepciones:
            - ValueError: si coordenada es invalida.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_coordenada(coordenada)
        nodo = (float(coordenada[0]), float(coordenada[1]))
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_calle(self, origen: Coordenada, destino: Coordenada, peso: float) -> bool:
        """
        Descripcion:
            Agrega una calle dirigida y ponderada.

        Parametros:
            origen (Coordenada): nodo de salida existente.
            destino (Coordenada): nodo de llegada existente.
            peso (float): costo positivo de la calle.

        Retorna:
            bool: True si la arista fue agregada, False si ya existia.

        Precondiciones:
            - origen y destino deben existir en el grafo.
            - peso debe ser positivo.

        Postcondiciones:
            - Si no existia, se crea la arista origen -> destino.

        Excepciones:
            - ValueError: si coordenadas o peso son invalidos.
            - KeyError: si origen o destino no existen.

        Complejidad temporal:
            O(d), donde d es el grado de salida del origen.

        Complejidad espacial:
            O(1)
        """
        self._validar_coordenada(origen)
        self._validar_coordenada(destino)
        if not isinstance(peso, (int, float)) or peso <= 0:
            raise ValueError("El peso debe ser un numero positivo.")
        if origen not in self.grafo:
            raise KeyError(f"El nodo origen no existe: {origen}")
        if destino not in self.grafo:
            raise KeyError(f"El nodo destino no existe: {destino}")

        for vecino, _ in self.grafo[origen]:
            if vecino == destino:
                return False
        self.grafo[origen].append((destino, float(peso)))
        return True

    def obtener_vecinos(self, coordenada: Coordenada) -> List[Tuple[Coordenada, float]]:
        """
        Descripcion:
            Retorna las calles salientes de una interseccion.

        Parametros:
            coordenada (Coordenada): nodo existente a consultar.

        Retorna:
            List[Tuple[Coordenada, float]]: vecinos y pesos asociados.

        Precondiciones:
            - coordenada debe existir en el grafo.

        Postcondiciones:
            - No modifica el grafo.

        Excepciones:
            - ValueError: si coordenada es invalida.
            - KeyError: si coordenada no existe.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_coordenada(coordenada)
        if coordenada not in self.grafo:
            raise KeyError(f"La interseccion no existe: {coordenada}")
        return self.grafo[coordenada]

    def cargar_desde_json(self, ruta_archivo: str) -> None:
        """
        Descripcion:
            Carga intersecciones y calles desde un archivo JSON.

        Parametros:
            ruta_archivo (str): ruta del archivo JSON.

        Retorna:
            None: reconstruye el grafo en sitio.

        Precondiciones:
            - ruta_archivo debe existir y contener claves intersecciones y calles.

        Postcondiciones:
            - El grafo contiene los nodos y aristas validos del JSON.

        Excepciones:
            - FileNotFoundError: si el archivo no existe.
            - KeyError: si faltan claves requeridas.
            - ValueError: si algun dato del JSON es invalido.
            - json.JSONDecodeError: si el JSON no es valido.

        Complejidad temporal:
            O(V + E)

        Complejidad espacial:
            O(V + E)
        """
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.grafo = {}
        for nodo_str in datos["intersecciones"]:
            latitud, longitud = map(float, nodo_str.split(","))
            self.agregar_interseccion((latitud, longitud))

        for calle in datos["calles"]:
            origen_lat, origen_lon = map(float, calle["origen"].split(","))
            destino_lat, destino_lon = map(float, calle["destino"].split(","))
            self.agregar_calle(
                (origen_lat, origen_lon),
                (destino_lat, destino_lon),
                float(calle["peso"]),
            )

    def cantidad_nodos(self) -> int:
        """
        Descripcion:
            Obtiene la cantidad de intersecciones del grafo.

        Parametros:
            Ninguno.

        Retorna:
            int: numero de nodos.

        Precondiciones:
            - Ninguna.

        Postcondiciones:
            - No modifica el grafo.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        return len(self.grafo)

    def cantidad_aristas(self) -> int:
        """
        Descripcion:
            Obtiene la cantidad de calles dirigidas del grafo.

        Parametros:
            Ninguno.

        Retorna:
            int: numero de aristas.

        Precondiciones:
            - Ninguna.

        Postcondiciones:
            - No modifica el grafo.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(V)

        Complejidad espacial:
            O(1)
        """
        return sum(len(vecinos) for vecinos in self.grafo.values())

    def existe_interseccion(self, coordenada: Coordenada) -> bool:
        """
        Descripcion:
            Indica si una coordenada existe como interseccion.

        Parametros:
            coordenada (Coordenada): coordenada a consultar.

        Retorna:
            bool: True si existe, False en caso contrario.

        Precondiciones:
            - coordenada debe contener dos numeros.

        Postcondiciones:
            - No modifica el grafo.

        Excepciones:
            - ValueError: si coordenada es invalida.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_coordenada(coordenada)
        return coordenada in self.grafo

    def __repr__(self) -> str:
        return f"RoadNetwork(Nodos={self.cantidad_nodos()}, Aristas={self.cantidad_aristas()})"
