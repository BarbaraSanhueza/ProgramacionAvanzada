#Dado un arreglo de enteros, encontrar los k números más pequeños usando heap.

import heapq
import time

start_time = time.perf_counter()

nums = [7, 2, 5, 1, 9, 3]
k = 3

heapq.heapify(nums)
print(f"Lista convertida en heap: {nums}")
print(f"Menor elemento: {nums[0]}")

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
