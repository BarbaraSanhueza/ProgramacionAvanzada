import time

# Clase que alberga a GridPaths con modificaciones de memoization para guardar los resultados anteriores
# Optimizando el tiempo de ejecucion

def count_paths(i, j, m, n, memo=None):

    if memo is None:
        memo = {}

    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0

    subproblema = (i, j)
    if subproblema in memo:
        return memo[subproblema]

    memo[subproblema] = (
        count_paths(i + 1, j, m, n, memo)
        + count_paths(i, j + 1, m, n, memo)
    )
    return memo[subproblema]


def run_test(m, n):
    start = time.time()
    result = count_paths(0, 0, m, n)
    end = time.time()

    print(f"Matriz {m}x{n}")
    print("Numero de caminos:", result)
    print("Tiempo de ejecucion:", end - start, "segundos")
    print()


if __name__ == "__main__":
    test_sizes = [(10, 10), (12, 12), (15, 15)]

    for m, n in test_sizes:
        run_test(m, n)
