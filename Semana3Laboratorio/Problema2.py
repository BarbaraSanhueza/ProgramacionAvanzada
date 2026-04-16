#Dado un arreglo de enteros, encontrar los k elementos más frecuentes usando heap.
from collections import Counter
import heapq
import time

start_time = time.perf_counter()

def topKFrecuentes (nums,k):
    counts = Counter(nums)
    return heapq.nlargest(k,counts.keys(), key=counts.get) 

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrecuentes(nums,k))

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")


