import time

# Clase que alberga a GridPaths sin modificaciónes.

def count_paths(i, j, m, n):
    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    return count_paths(i + 1, j, m, n) + count_paths(i, j + 1, m, n)


def run_test(m, n):
    start = time.time()
    result = count_paths(0, 0, m, n)
    end = time.time()

    print(f"Matriz {m}x{n}")
    print("Número de caminos:", result)
    print("Tiempo de ejecución:", end - start, "segundos")
    print()


if __name__ == "__main__":
    test_sizes = [(10, 10), (12, 12), (15, 15)]

    for m, n in test_sizes:
        run_test(m, n)
