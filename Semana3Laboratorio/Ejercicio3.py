#Dado un conjunto de productos con puntajes, devolver los Top-K productos más relevantes.

#Ejemplo:
#productos = [("Laptop", 95), ("Mouse", 80), ("Teclado", 85)]
#k = 2
#Salida esperada: ['Laptop', 'Teclado']

import heapq
import time

start_time = time.perf_counter()


productos = [("Laptop", 95), ("Mouse", 80), ("Teclado", 85)]

k = 2

heapq.heapify(productos)

topKProductos = heapq.nlargest(k, productos, key = lambda x: x[1])

topProductos = [item[0] for item in topKProductos]
print(topProductos)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")


