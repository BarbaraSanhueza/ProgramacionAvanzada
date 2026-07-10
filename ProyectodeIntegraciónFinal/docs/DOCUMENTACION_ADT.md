# Documentacion de ADT

## Incident

**Proposito:** representar un incidente de emergencia con datos minimos para hashing, priorizacion, reportes y asignacion de rutas.

**Representacion interna:** objeto con `id`, `zona`, `ubicacion`, `prioridad`, `tipo`, `timestamp` y `estado`.

**Invariantes:** los textos obligatorios no son vacios; `ubicacion` contiene latitud y longitud numericas; `prioridad` pertenece a Baja, Media, Alta o Critica/Crítica; `timestamp` usa `YYYY-MM-DD HH:MM:SS`; el estado inicial es `Pendiente`.

**Responsabilidades:** validar datos de incidente, permitir actualizar estado, permitir cambiar prioridad y exponer la fecha como `datetime`.

| Operacion | Precondiciones | Postcondiciones | Complejidad temporal | Complejidad espacial |
|---|---|---|---|---|
| `__init__` | Datos obligatorios validos | Incidente creado en estado Pendiente | O(1) | O(1) |
| `actualizar_estado` | Estado no vacio | Estado actualizado | O(1) | O(1) |
| `cambiar_prioridad` | Prioridad valida | Prioridad actualizada | O(1) | O(1) |
| `fecha_datetime` | Timestamp con formato valido | Retorna `datetime` sin modificar el objeto | O(1) | O(1) |

## EmergencyCenter

**Proposito:** representar un centro de emergencia desde donde se despachan recursos.

**Representacion interna:** objeto con `id`, `nombre` y `ubicacion`.

**Invariantes:** `id` y `nombre` son cadenas no vacias; `ubicacion` contiene dos numeros.

**Responsabilidades:** validar datos del centro y servir como origen de rutas en la red vial.

| Operacion | Precondiciones | Postcondiciones | Complejidad temporal | Complejidad espacial |
|---|---|---|---|---|
| `__init__` | Identificador, nombre y ubicacion validos | Centro creado | O(1) | O(1) |
| `__repr__` | Centro inicializado | Retorna representacion textual | O(1) | O(1) |

## RoadNetwork

**Proposito:** representar una red vial dirigida y ponderada para busqueda de rutas.

**Representacion interna:** lista de adyacencia con `dict[coordenada] -> list[(vecino, peso)]`.

**Invariantes:** todo nodo destino existe; los pesos son positivos; no hay aristas duplicadas con mismo origen y destino.

**Responsabilidades:** administrar nodos y aristas, validar la integridad del grafo, cargar JSON y exponer metricas.

| Operacion | Precondiciones | Postcondiciones | Complejidad temporal | Complejidad espacial |
|---|---|---|---|---|
| `__init__` | Ninguna | Grafo vacio | O(1) | O(1) |
| `agregar_interseccion` | Coordenada valida | Nodo existe en el grafo | O(1) | O(1) |
| `agregar_calle` | Origen y destino existentes, peso positivo | Arista agregada si no estaba duplicada | O(d) | O(1) |
| `obtener_vecinos` | Coordenada existente | Retorna calles salientes | O(1) | O(1) |
| `cargar_desde_json` | Archivo JSON valido | Grafo reconstruido | O(V + E) | O(V + E) |
| `cantidad_nodos` | Ninguna | Retorna numero de nodos | O(1) | O(1) |
| `cantidad_aristas` | Ninguna | Retorna numero de aristas | O(V) | O(1) |
| `existe_interseccion` | Coordenada valida | Retorna existencia del nodo | O(1) | O(1) |

## Observaciones

La tabla hash y el Max-Heap no reemplazan estos ADT: los consumen. La tabla hash usa lista de buckets propia y el heap usa lista propia con operaciones de subida y bajada.
