from datetime import datetime
from typing import Any, List, Tuple

from Incident import Incident


class IncidentPriorityQueue:
    """Cola de prioridad Max-Heap propia basada en lista."""

    VALORES_SEVERIDAD = {"Baja": 1, "Media": 2, "Alta": 3, "Critica": 4, "Crítica": 4}

    def __init__(self) -> None:
        """
        Descripcion:
            Inicializa una cola de prioridad vacia.

        Parametros:
            Ninguno.

        Retorna:
            None: el constructor no retorna valor.

        Precondiciones:
            - Ninguna.

        Postcondiciones:
            - heap queda inicializado como lista vacia.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        self.heap: List[Tuple[float, Any]] = []

    def _calcular_prioridad_numerica(self, incidente: Any) -> float:
        """
        Descripcion:
            Calcula urgencia = severidad x (1 + horas_de_espera).

        Parametros:
            incidente (Any): objeto con prioridad y timestamp.

        Retorna:
            float: valor de urgencia.

        Precondiciones:
            - incidente debe tener prioridad valida y timestamp completo.

        Postcondiciones:
            - No modifica el incidente.

        Excepciones:
            - ValueError: si el timestamp o la prioridad son invalidos.

        Complejidad temporal:
            O(1)

        Complejidad espacial:
            O(1)
        """
        severidad = self.VALORES_SEVERIDAD.get(incidente.prioridad)
        if severidad is None:
            raise ValueError("Prioridad invalida para calcular urgencia.")
        fecha_incidente = Incident.validar_timestamp(incidente.timestamp)
        horas_espera = (datetime.now() - fecha_incidente).total_seconds() / 3600
        if horas_espera < 0:
            horas_espera = 0.0
        return float(severidad * (1 + horas_espera))

    def _subir(self, posicion: int) -> None:
        while posicion > 0:
            padre = (posicion - 1) // 2
            if self.heap[posicion][0] <= self.heap[padre][0]:
                break
            self.heap[posicion], self.heap[padre] = self.heap[padre], self.heap[posicion]
            posicion = padre

    def _bajar(self, posicion: int) -> None:
        tamano = len(self.heap)
        while True:
            hijo_izq = 2 * posicion + 1
            hijo_der = 2 * posicion + 2
            mayor = posicion
            if hijo_izq < tamano and self.heap[hijo_izq][0] > self.heap[mayor][0]:
                mayor = hijo_izq
            if hijo_der < tamano and self.heap[hijo_der][0] > self.heap[mayor][0]:
                mayor = hijo_der
            if mayor == posicion:
                break
            self.heap[posicion], self.heap[mayor] = self.heap[mayor], self.heap[posicion]
            posicion = mayor

    def insertar(self, incidente: Any) -> None:
        """
        Descripcion:
            Inserta un incidente en el Max-Heap.

        Parametros:
            incidente (Any): incidente valido.

        Retorna:
            None: modifica el heap en sitio.

        Precondiciones:
            - incidente debe tener id, prioridad y timestamp validos.

        Postcondiciones:
            - El heap conserva la propiedad de maximo.

        Excepciones:
            - ValueError: si los datos del incidente no permiten calcular urgencia.

        Complejidad temporal:
            O(log n)

        Complejidad espacial:
            O(1)
        """
        urgencia = self._calcular_prioridad_numerica(incidente)
        self.heap.append((urgencia, incidente))
        self._subir(len(self.heap) - 1)

    def extraer_maximo(self) -> Any:
        """
        Descripcion:
            Extrae el incidente con mayor urgencia.

        Parametros:
            Ninguno.

        Retorna:
            Any: incidente mas urgente o None si la cola esta vacia.

        Precondiciones:
            - Ninguna.

        Postcondiciones:
            - Si habia elementos, se elimina exactamente el maximo.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(log n)

        Complejidad espacial:
            O(1)
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        maximo = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self._bajar(0)
        return maximo

    def actualizar_prioridad(self, id_incidente: str, nueva_prioridad: str) -> bool:
        """
        Descripcion:
            Cambia la prioridad de un incidente y restaura el heap.

        Parametros:
            id_incidente (str): ID buscado.
            nueva_prioridad (str): prioridad permitida.

        Retorna:
            bool: True si actualizo, False si no encontro el incidente.

        Precondiciones:
            - id_incidente debe ser cadena no vacia.
            - nueva_prioridad debe ser valida para Incident.

        Postcondiciones:
            - Si existe, el incidente cambia prioridad y el heap queda valido.

        Excepciones:
            - ValueError: si nueva_prioridad es invalida.

        Complejidad temporal:
            O(n)

        Complejidad espacial:
            O(1)
        """
        if not isinstance(id_incidente, str) or not id_incidente.strip():
            raise ValueError("id_incidente debe ser una cadena no vacia.")
        for posicion, (_, incidente) in enumerate(self.heap):
            if incidente.id == id_incidente:
                incidente.cambiar_prioridad(nueva_prioridad)
                self.heap[posicion] = (self._calcular_prioridad_numerica(incidente), incidente)
                self._subir(posicion)
                self._bajar(posicion)
                return True
        return False

    def mostrar_top_k(self, k: int) -> List[Any]:
        """
        Descripcion:
            Retorna los k incidentes mas urgentes sin eliminarlos.

        Parametros:
            k (int): cantidad de incidentes a mostrar.

        Retorna:
            List[Any]: incidentes ordenados por urgencia descendente.

        Precondiciones:
            - k debe ser mayor o igual que cero.

        Postcondiciones:
            - El heap original no se modifica.

        Excepciones:
            - ValueError: si k es negativo o no entero.

        Complejidad temporal:
            O(k n)

        Complejidad espacial:
            O(k)
        """
        if not isinstance(k, int) or k < 0:
            raise ValueError("k debe ser un entero no negativo.")
        seleccionados: List[Any] = []
        indices_usados = set()
        limite = min(k, len(self.heap))
        for _ in range(limite):
            mejor_indice = -1
            mejor_valor = float("-inf")
            for indice, (urgencia, _) in enumerate(self.heap):
                if indice not in indices_usados and urgencia > mejor_valor:
                    mejor_valor = urgencia
                    mejor_indice = indice
            if mejor_indice == -1:
                break
            indices_usados.add(mejor_indice)
            seleccionados.append(self.heap[mejor_indice][1])
        return seleccionados

    def obtener_urgencia(self, incidente: Any) -> float:
        """Retorna la urgencia actual de un incidente. Tiempo O(1), espacio O(1)."""
        return self._calcular_prioridad_numerica(incidente)

    def __repr__(self) -> str:
        return f"PriorityQueue(Incidentes en cola={len(self.heap)})"
