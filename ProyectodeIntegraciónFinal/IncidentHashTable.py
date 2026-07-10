from typing import Any, List, Optional, Tuple


class IncidentHashTable:
    """Tabla hash propia para incidentes mediante lista de buckets."""

    def __init__(self, capacidad_inicial: int = 100) -> None:
        """
        Descripcion:
            Inicializa una tabla hash con encadenamiento separado.

        Parametros:
            capacidad_inicial (int): cantidad de buckets.

        Retorna:
            None: el constructor no retorna valor.

        Precondiciones:
            - capacidad_inicial debe ser mayor que cero.

        Postcondiciones:
            - La tabla queda vacia con capacidad fija inicial.

        Excepciones:
            - ValueError: si capacidad_inicial no es positiva.

        Complejidad temporal:
            O(m), donde m es la capacidad.

        Complejidad espacial:
            O(m)
        """
        if not isinstance(capacidad_inicial, int) or capacidad_inicial <= 0:
            raise ValueError("capacidad_inicial debe ser un entero positivo.")
        self.capacidad: int = capacidad_inicial
        self.tabla: List[List[Tuple[str, Any]]] = [[] for _ in range(self.capacidad)]
        self.total_elementos: int = 0
        self.colisiones: int = 0

    def _hash(self, id_incidente: str) -> int:
        """Hash polinomial propio. Tiempo O(k), espacio O(1)."""
        if not isinstance(id_incidente, str) or not id_incidente.strip():
            raise ValueError("id_incidente debe ser una cadena no vacia.")
        acumulado = 0
        base = 31
        for caracter in id_incidente:
            acumulado = (acumulado * base + ord(caracter)) % self.capacidad
        return acumulado

    def _recalcular_colisiones(self) -> None:
        self.colisiones = sum(max(0, len(bucket) - 1) for bucket in self.tabla)

    def insertar(self, incidente: Any) -> None:
        """
        Descripcion:
            Inserta un incidente o actualiza el existente con el mismo ID.

        Parametros:
            incidente (Any): objeto con atributo id.

        Retorna:
            None: modifica la tabla en sitio.

        Precondiciones:
            - incidente debe tener un atributo id valido.

        Postcondiciones:
            - El incidente queda disponible por su ID sin duplicados.

        Excepciones:
            - ValueError: si incidente o su id son invalidos.

        Complejidad temporal:
            O(1) promedio, O(n) peor caso.

        Complejidad espacial:
            O(1)
        """
        if not hasattr(incidente, "id"):
            raise ValueError("incidente debe tener atributo id.")
        indice = self._hash(incidente.id)
        bucket = self.tabla[indice]

        for posicion, (id_existente, _) in enumerate(bucket):
            if id_existente == incidente.id:
                bucket[posicion] = (incidente.id, incidente)
                self._recalcular_colisiones()
                return

        bucket.append((incidente.id, incidente))
        self.total_elementos += 1
        self._recalcular_colisiones()

    def buscar(self, id_incidente: str) -> Optional[Any]:
        """
        Descripcion:
            Busca un incidente por ID.

        Parametros:
            id_incidente (str): identificador a buscar.

        Retorna:
            Optional[Any]: incidente encontrado o None.

        Precondiciones:
            - id_incidente debe ser una cadena no vacia.

        Postcondiciones:
            - No modifica la tabla.

        Excepciones:
            - ValueError: si id_incidente es invalido.

        Complejidad temporal:
            O(1) promedio, O(n) peor caso.

        Complejidad espacial:
            O(1)
        """
        indice = self._hash(id_incidente)
        for id_existente, incidente in self.tabla[indice]:
            if id_existente == id_incidente:
                return incidente
        return None

    def actualizar_estado(self, id_incidente: str, nuevo_estado: str) -> bool:
        """
        Descripcion:
            Actualiza el estado de un incidente almacenado.

        Parametros:
            id_incidente (str): identificador del incidente.
            nuevo_estado (str): estado no vacio.

        Retorna:
            bool: True si actualizo, False si no encontro el ID.

        Precondiciones:
            - id_incidente y nuevo_estado deben ser cadenas validas.

        Postcondiciones:
            - Si existe, el estado queda actualizado.

        Excepciones:
            - ValueError: si id_incidente es invalido o el incidente rechaza el estado.

        Complejidad temporal:
            O(1) promedio, O(n) peor caso.

        Complejidad espacial:
            O(1)
        """
        incidente = self.buscar(id_incidente)
        if incidente is None:
            return False
        incidente.actualizar_estado(nuevo_estado)
        return True

    def eliminar(self, id_incidente: str) -> bool:
        """
        Descripcion:
            Elimina un incidente por ID.

        Parametros:
            id_incidente (str): identificador a eliminar.

        Retorna:
            bool: True si elimino, False si no encontro el ID.

        Precondiciones:
            - id_incidente debe ser una cadena no vacia.

        Postcondiciones:
            - Si existia, el incidente deja de estar en la tabla.

        Excepciones:
            - ValueError: si id_incidente es invalido.

        Complejidad temporal:
            O(1) promedio, O(n) peor caso.

        Complejidad espacial:
            O(1)
        """
        indice = self._hash(id_incidente)
        bucket = self.tabla[indice]
        for posicion, (id_existente, _) in enumerate(bucket):
            if id_existente == id_incidente:
                bucket.pop(posicion)
                self.total_elementos -= 1
                self._recalcular_colisiones()
                return True
        return False

    def obtener_estadisticas(self) -> dict:
        """
        Descripcion:
            Calcula estadisticas de distribucion de la tabla.

        Parametros:
            Ninguno.

        Retorna:
            dict: factor de carga, colisiones, buckets utilizados y maximo bucket.

        Precondiciones:
            - La tabla debe estar inicializada.

        Postcondiciones:
            - No modifica los incidentes almacenados.

        Excepciones:
            - Ninguna.

        Complejidad temporal:
            O(m), donde m es la capacidad.

        Complejidad espacial:
            O(1)
        """
        buckets_utilizados = 0
        max_tamano_bucket = 0
        colisiones = 0
        for bucket in self.tabla:
            tamano = len(bucket)
            if tamano > 0:
                buckets_utilizados += 1
                colisiones += tamano - 1
            if tamano > max_tamano_bucket:
                max_tamano_bucket = tamano
        self.colisiones = colisiones
        return {
            "Factor de carga": round(self.total_elementos / self.capacidad, 4),
            "Colisiones": self.colisiones,
            "Buckets utilizados": buckets_utilizados,
            "Maximo tamano de bucket": max_tamano_bucket,
        }
