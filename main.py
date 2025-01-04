import time
from src.generator import generate_data
from src.utils import build_distance_matrix
from src.bruteforce import bruteforce
from src.greedy import greedy
from src.greedy_randomized import greedy_randomized
from src.nearest_neighbor import nearest_neighbor
from src.simulated_annealing import simulated_annealing


def run_benchmark(n: int = 10):
    data_file = f"data/sample_n{n}.json"
    generate_data(data_file, n)
    matrix, paczkomaty = build_distance_matrix(data_file)

    algorithms = [
        ("Greedy", greedy),
        ("Greedy Randomized", greedy_randomized),
        ("Nearest Neighbor", nearest_neighbor),
        ("Simulated Annealing", simulated_annealing),
    ]
    if n <= 10:
        algorithms.insert(0, ("Bruteforce", bruteforce))

    print(f"=== Modified VRP Benchmark (n={n} paczkomatow) ===")
    for name, func in algorithms:
        start = time.perf_counter()
        route, packages, route_time = func(matrix, paczkomaty)
        elapsed = time.perf_counter() - start
        print(f"\n[{name}]")
        print(f"  Packages: {packages} | Route time: {route_time:.2f} h | Exec: {elapsed:.5f} s")
        print(f"  Route:    {route}")


if __name__ == "__main__":
    run_benchmark(n=10)