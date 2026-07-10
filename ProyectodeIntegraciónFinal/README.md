# Sistema Inteligente de Gestion y Optimizacion de Rutas de Emergencia

## Descripcion

Proyecto Python que modela incidentes, centros de emergencia y una red vial dirigida para priorizar emergencias, seleccionar centros por costo de ruta y generar reportes ordenados.

## Objetivo

Integrar ADT, hashing propio, Max-Heap propio, algoritmos de sorting manuales y busqueda en grafos para simular un sistema de despacho de emergencias.

## Requisitos

- Python 3.10 o superior.
- Sin librerias externas.
- Ejecutar desde la carpeta del proyecto.

## Estructura de archivos

- `Incident.py`: ADT de incidente.
- `EmergencyCenter.py`: ADT de centro de emergencia.
- `RoadNetwork.py`: ADT de red vial dirigida y ponderada.
- `IncidentHashTable.py`: tabla hash propia con buckets.
- `IncidentPriorityQueue.py`: Max-Heap propio.
- `IncidentSorter.py`: QuickSort y MergeSort manuales.
- `RouteFinder.py`: BFS, Dijkstra/UCS y A* como bonificacion.
- `reportes.py`: reportes ordenados.
- `main.py`: escenario integrado.
- `test_sorting.py`: prueba basica de ordenamiento.
- `test_experimentos.py`: experimentacion completa.
- `incidentes.csv`: dataset con 500 incidentes.
- `DOCUMENTACION_ADT.md`: documentacion formal de ADT.

## ADT

`Incident` valida ID, zona, ubicacion, prioridad, tipo y fecha completa. `EmergencyCenter` valida identificador, nombre y ubicacion. `RoadNetwork` mantiene un grafo dirigido ponderado por lista de adyacencia y valida nodos, pesos positivos y duplicados.

## Hashing

`IncidentHashTable` usa una lista de buckets y una funcion hash polinomial propia. La insercion actualiza IDs existentes sin duplicarlos. Reporta factor de carga, colisiones, buckets utilizados y maximo tamano de bucket.

## Max-Heap

`IncidentPriorityQueue` usa una lista propia, sin `heapq`. La urgencia se calcula como:

```text
urgencia = severidad * (1 + horas_de_espera)
```

La severidad usa Baja=1, Media=2, Alta=3 y Critica/Crítica=4. Los tiempos negativos se convierten a cero.

## Sorting

`IncidentSorter` conserva QuickSort y MergeSort manuales con parametro `key`. Los reportes usan estos algoritmos y no `sorted()` ni `list.sort()`.

## Grafos

`RouteFinder` implementa BFS y Dijkstra/UCS. BFS ignora pesos durante la busqueda y calcula despues el costo real de la ruta. Dijkstra minimiza costo acumulado con `heapq`. A* se incluye como bonificacion con heuristica cero para no sobreestimar cuando los pesos representan minutos.

## Dataset

`incidentes.csv` usa las columnas:

```text
ID,Zona,Latitud,Longitud,Prioridad,Tipo,Fecha
```

La fecha usa `YYYY-MM-DD HH:MM:SS`. Si el archivo no existe, esta vacio, tiene formato antiguo o datos invalidos, `main.py` lo regenera con `random.seed(42)`.

## Ejecucion

```bash
python main.py
```

Ejecuta el escenario integrado: crea red vial de 50 nodos, valida al menos 100 aristas, carga 500 incidentes, inserta en hash y heap, selecciona centro por Dijkstra y genera reportes.

## Experimentacion

```bash
python test_sorting.py
python test_experimentos.py
```

`test_experimentos.py` mide hashing, heap, sorting y grafos usando `time.perf_counter()`.

## Salidas esperadas

- Estadisticas del hash.
- Top-K de incidentes criticos.
- Incidente mas urgente extraido.
- Centro asignado por menor costo acumulado.
- Ruta sugerida, nodos visitados, distancia, costo y tiempo estimado.
- Reportes de incidentes antiguos, criticos y zonas con mas incidentes.

## Limitaciones conocidas

- La red vial es simulada y no representa calles reales.
- Los pesos del grafo se interpretan como minutos aproximados.
- A* usa heuristica cero para mantener admisibilidad; por eso se comporta como una variante de Dijkstra.
- La urgencia depende del reloj del sistema al ejecutar.
