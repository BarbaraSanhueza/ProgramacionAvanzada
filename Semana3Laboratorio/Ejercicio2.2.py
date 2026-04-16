#Ejercicio 2.2: Mezclar k listas ordenadas.
#Entrada: [[1,4,5],[1,3,4],[2,6]]
#Salida: [1,1,2,3,4,4,5,6]

import heapq
import time

start_time = time.perf_counter()

entrada = [[1,4,5],[1,3,4],[2,6]]
resultado = heapq.merge(*entrada)
listaFinal = list(resultado)
print(listaFinal)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
