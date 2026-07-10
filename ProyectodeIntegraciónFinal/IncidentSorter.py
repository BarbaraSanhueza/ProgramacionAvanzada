from typing import Any, Callable, List


class IncidentSorter:
    """Implementaciones manuales de QuickSort y MergeSort con parametro key."""

    @staticmethod
    def quicksort(lista: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        """
        Descripcion:
            Ordena una lista con QuickSort funcional no in-place.

        Parametros:
            lista (List[Any]): elementos a ordenar.
            key (Callable[[Any], Any]): funcion que obtiene la clave de orden.

        Retorna:
            List[Any]: nueva lista ordenada ascendentemente.

        Precondiciones:
            - key debe poder aplicarse a todos los elementos.

        Postcondiciones:
            - La lista original no se modifica.

        Excepciones:
            - TypeError: si key no permite comparar claves.

        Complejidad temporal:
            Mejor caso O(n log n), promedio O(n log n), peor caso O(n^2).

        Complejidad espacial:
            O(n log n) promedio por particiones y recursion; O(n^2) peor caso.

        Estabilidad:
            Estable en esta implementacion porque preserva el orden de iguales.

        In-place:
            No trabaja in-place.
        """
        if len(lista) <= 1:
            return list(lista)
        pivote = lista[len(lista) // 2]
        valor_pivote = key(pivote)
        menores = [elemento for elemento in lista if key(elemento) < valor_pivote]
        iguales = [elemento for elemento in lista if key(elemento) == valor_pivote]
        mayores = [elemento for elemento in lista if key(elemento) > valor_pivote]
        return (
            IncidentSorter.quicksort(menores, key)
            + iguales
            + IncidentSorter.quicksort(mayores, key)
        )

    @staticmethod
    def mergesort(lista: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        """
        Descripcion:
            Ordena una lista con MergeSort.

        Parametros:
            lista (List[Any]): elementos a ordenar.
            key (Callable[[Any], Any]): funcion que obtiene la clave de orden.

        Retorna:
            List[Any]: nueva lista ordenada ascendentemente.

        Precondiciones:
            - key debe poder aplicarse a todos los elementos.

        Postcondiciones:
            - La lista original no se modifica.

        Excepciones:
            - TypeError: si key no permite comparar claves.

        Complejidad temporal:
            Mejor caso O(n log n), promedio O(n log n), peor caso O(n log n).

        Complejidad espacial:
            O(n) auxiliar mas O(log n) por recursion.

        Estabilidad:
            Estable.

        In-place:
            No trabaja in-place.
        """
        if len(lista) <= 1:
            return list(lista)
        medio = len(lista) // 2
        izquierda = IncidentSorter.mergesort(lista[:medio], key)
        derecha = IncidentSorter.mergesort(lista[medio:], key)
        return IncidentSorter._merge(izquierda, derecha, key)

    @staticmethod
    def _merge(izquierda: List[Any], derecha: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        """Mezcla dos listas ya ordenadas. Tiempo O(n), espacio O(n)."""
        resultado: List[Any] = []
        i = 0
        j = 0
        while i < len(izquierda) and j < len(derecha):
            if key(izquierda[i]) <= key(derecha[j]):
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado
