from datetime import datetime
from typing import Tuple


class Incident:
    """
    ADT Incident.

    Proposito:
        Representar un incidente de emergencia que debe ser indexado,
        priorizado y asignado a un centro de despacho.

    Representacion interna:
        Objeto con atributos simples: id, zona, ubicacion, prioridad, tipo,
        timestamp y estado.

    Atributos:
        id (str): identificador unico del incidente.
        zona (str): zona operacional del incidente.
        ubicacion (Tuple[float, float]): coordenadas (latitud, longitud).
        prioridad (str): Baja, Media, Alta o Critica/Crítica.
        tipo (str): categoria descriptiva del incidente.
        timestamp (str): fecha y hora en formato YYYY-MM-DD HH:MM:SS.
        estado (str): estado operacional del incidente.

    Invariantes:
        - id, zona, prioridad, tipo, timestamp y estado son cadenas no vacias.
        - ubicacion contiene dos numeros reales.
        - prioridad pertenece al conjunto permitido.
        - timestamp usa el formato YYYY-MM-DD HH:MM:SS.
        - estado inicial es Pendiente.

    Responsabilidades:
        - Validar datos minimos del incidente.
        - Exponer operaciones para cambiar estado y prioridad.
    """

    PRIORIDADES_VALIDAS = {"Baja", "Media", "Alta", "Critica", "Crítica"}
    FORMATO_FECHA = "%Y-%m-%d %H:%M:%S"

    def __init__(
        self,
        id_incidente: str,
        zona: str,
        ubicacion: Tuple[float, float],
        prioridad: str,
        tipo: str,
        timestamp: str,
    ) -> None:
        """
        Descripcion:
            Crea un incidente validado con estado inicial Pendiente.

        Parametros:
            id_incidente (str): identificador unico no vacio.
            zona (str): zona no vacia del incidente.
            ubicacion (Tuple[float, float]): coordenadas (latitud, longitud).
            prioridad (str): prioridad permitida.
            tipo (str): tipo no vacio del incidente.
            timestamp (str): fecha completa en formato YYYY-MM-DD HH:MM:SS.

        Retorna:
            None: el constructor no retorna valor.

        Precondiciones:
            - id_incidente, zona, prioridad, tipo y timestamp deben ser cadenas.
            - ubicacion debe contener dos valores numericos.

        Postcondiciones:
            - El incidente queda creado con estado Pendiente.

        Excepciones:
            - ValueError: si algun dato obligatorio es invalido.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_texto(id_incidente, "ID")
        self._validar_texto(zona, "zona")
        self._validar_ubicacion(ubicacion)
        self._validar_prioridad(prioridad)
        self._validar_texto(tipo, "tipo")
        self.validar_timestamp(timestamp)

        self.id: str = id_incidente.strip()
        self.zona: str = zona.strip()
        self.ubicacion: Tuple[float, float] = (float(ubicacion[0]), float(ubicacion[1]))
        self.prioridad: str = prioridad.strip()
        self.tipo: str = tipo.strip()
        self.timestamp: str = timestamp.strip()
        self.estado: str = "Pendiente"

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

    @classmethod
    def _validar_prioridad(cls, prioridad: str) -> None:
        cls._validar_texto(prioridad, "prioridad")
        if prioridad.strip() not in cls.PRIORIDADES_VALIDAS:
            raise ValueError("prioridad debe ser Baja, Media, Alta o Critica/Crítica.")

    @classmethod
    def validar_timestamp(cls, timestamp: str) -> datetime:
        cls._validar_texto(timestamp, "timestamp")
        try:
            return datetime.strptime(timestamp.strip(), cls.FORMATO_FECHA)
        except ValueError as exc:
            raise ValueError("timestamp debe usar el formato YYYY-MM-DD HH:MM:SS.") from exc

    def actualizar_estado(self, nuevo_estado: str) -> None:
        """
        Descripcion:
            Actualiza el estado operacional del incidente.

        Parametros:
            nuevo_estado (str): nuevo estado no vacio.

        Retorna:
            None: modifica el objeto en sitio.

        Precondiciones:
            - nuevo_estado debe ser una cadena no vacia.

        Postcondiciones:
            - estado queda actualizado.

        Excepciones:
            - ValueError: si nuevo_estado es invalido.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_texto(nuevo_estado, "nuevo_estado")
        self.estado = nuevo_estado.strip()

    def cambiar_prioridad(self, nueva_prioridad: str) -> None:
        """
        Descripcion:
            Cambia la prioridad del incidente.

        Parametros:
            nueva_prioridad (str): prioridad permitida.

        Retorna:
            None: modifica el objeto en sitio.

        Precondiciones:
            - nueva_prioridad debe pertenecer al conjunto permitido.

        Postcondiciones:
            - prioridad queda actualizada.

        Excepciones:
            - ValueError: si la prioridad es invalida.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self._validar_prioridad(nueva_prioridad)
        self.prioridad = nueva_prioridad.strip()

    def fecha_datetime(self) -> datetime:
        """
        Descripcion:
            Convierte el timestamp del incidente a datetime.

        Parametros:
            Ninguno.

        Retorna:
            datetime: fecha y hora del incidente.

        Precondiciones:
            - timestamp mantiene el formato validado.

        Postcondiciones:
            - No modifica el incidente.

        Excepciones:
            - ValueError: si timestamp fue alterado a un formato invalido.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        return self.validar_timestamp(self.timestamp)

    def __repr__(self) -> str:
        return (
            f"Incident(ID={self.id}, Zona={self.zona}, Tipo={self.tipo}, "
            f"Prioridad={self.prioridad}, Fecha={self.timestamp}, Estado={self.estado}, "
            f"Ubicacion={self.ubicacion})"
        )
