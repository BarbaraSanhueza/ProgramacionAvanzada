#Dado un arreglo de enteros, encontrar los k números más pequeños usando heap.

import time

start_time = time.perf_counter()

nums = [7, 2, 5, 1, 9, 3]
k = 3

numsMenores = sorted(nums)[:k]
print(numsMenores)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
