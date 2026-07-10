from typing import Tuple


class EmergencyCenter:
    """
    ADT EmergencyCenter.

    Proposito:
        Representar un centro de emergencia desde el cual se despachan recursos.

    Representacion interna:
        Objeto con identificador, nombre y ubicacion en un nodo de la red vial.

    Atributos:
        id (str): identificador unico del centro.
        nombre (str): nombre descriptivo del centro.
        ubicacion (Tuple[float, float]): nodo de la red donde se ubica.

    Invariantes:
        - id y nombre son cadenas no vacias.
        - ubicacion contiene dos numeros reales.

    Responsabilidades:
        - Validar y exponer los datos del centro.
        - Ser usado como origen para calcular rutas por grafo.
    """

    def __init__(self, id: str, nombre: str, ubicacion: Tuple[float, float]) -> None:
        """
        Descripcion:
            Crea un centro de emergencia validado.

        Parametros:
            id (str): identificador no vacio.
            nombre (str): nombre no vacio.
            ubicacion (Tuple[float, float]): coordenadas del nodo del centro.

        Retorna:
            None: el constructor no retorna valor.

        Precondiciones:
            - id y nombre deben ser cadenas no vacias.
            - ubicacion debe contener dos numeros.

        Postcondiciones:
            - El centro queda creado con id, nombre y ubicacion.

        Excepciones:
            - ValueError: si algun dato es invalido.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_texto(id, "id")
        self._validar_texto(nombre, "nombre")
        self._validar_ubicacion(ubicacion)
        self.id: str = id.strip()
        self.nombre: str = nombre.strip()
        self.ubicacion: Tuple[float, float] = (float(ubicacion[0]), float(ubicacion[1]))

    @staticmethod
    def _validar_texto(valor: str, nombre: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{nombre} debe ser una cadena no vacia.")

    @staticmethod
    def _validar_ubicacion(ubicacion: Tuple[float, float]) -> None:
        if not isinstance(ubicacion, tuple) or len(ubicacion) != 2:
            raise ValueError("ubicacion debe ser una tupla (latitud, longitud).")
        latitud, longitud = ubicacion
        if not isinstance(latitud, (int, float)) or not isinstance(longitud, (int, float)):
            raise ValueError("latitud y longitud deben ser numericas.")

    def __repr__(self) -> str:
        return f"EmergencyCenter(ID={self.id}, Nombre={self.nombre}, Ubicacion={self.ubicacion})"
