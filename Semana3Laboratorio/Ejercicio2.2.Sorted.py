#Ejercicio 2.2: Mezclar k listas ordenadas.
#Entrada: [[1,4,5],[1,3,4],[2,6]]
#Salida: [1,1,2,3,4,4,5,6]
import time

start_time = time.perf_counter()

import heapq

entrada = [[1,4,5],[1,3,4],[2,6]]


resultado = [item for sublist in entrada for item in sublist]


listaFinal = sorted(resultado)
print(listaFinal)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

