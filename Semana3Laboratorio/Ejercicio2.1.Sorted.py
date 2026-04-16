#Ejercicio 2.1: Dado un arreglo, encontrar el k-ésimo número más grande.
#Entrada: nums = [3,2,1,5,6,4], k=2
#Salida: 5
import time

start_time = time.perf_counter()

nums = [3,2,1,5,6,4]
k = 2

numsOrdenados = sorted(nums, reverse = True)

result = numsOrdenados[k-1]


print("El segundo k-enesimo mas grande es:", result)

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
