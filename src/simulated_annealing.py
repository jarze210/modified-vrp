import math
import random


def evaluate_solution(solution, distance_matrix, paczkomaty, speed=30.0, max_time=8.0):
    total_time = 0.0
    delivered_packages = 0

    for i in range(1, len(solution)):
        total_time += distance_matrix[solution[i - 1]][solution[i]] / speed
        if total_time > max_time:
            return 0, float("inf")
        if solution[i] != 0:
            delivered_packages += paczkomaty[solution[i]]["liczba_paczek"]

    return delivered_packages, total_time


def simulated_annealing(
    distance_matrix,
    paczkomaty,
    initial_temperature=100.0,
    cooling_rate=0.997,
    max_iterations=10000,
    max_time=8.0,
    speed=30.0,
):
    num_paczkomaty = len(paczkomaty)

    # Losowanie dopuszczalnego rozwiazania poczatkowego
    while True:
        subset_size = max(1, min(num_paczkomaty, int(0.25 * num_paczkomaty)))
        subset = random.sample(range(1, num_paczkomaty + 1), subset_size)
        current_solution = [0] + subset + [0]
        delivered_packages, current_time = evaluate_solution(
            current_solution, distance_matrix, paczkomaty, speed, max_time
        )
        if current_time <= max_time:
            break

    best_solution = current_solution[:]
    best_packages = delivered_packages
    best_time = current_time
    temperature = initial_temperature

    for _ in range(max_iterations):
        new_solution = current_solution[:]

        if len(new_solution) > 3 and random.random() < 0.5:
            i, j = random.sample(range(1, len(new_solution) - 1), 2)
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        else:
            if len(new_solution) > 3 and random.random() < 0.5:
                remove_idx = random.choice(range(1, len(new_solution) - 1))
                new_solution.pop(remove_idx)
            elif len(new_solution) < num_paczkomaty + 2:
                available = [
                    p for p in range(1, num_paczkomaty + 1) if p not in new_solution
                ]
                if available:
                    insert_pos = random.randint(1, len(new_solution) - 1)
                    new_solution.insert(insert_pos, random.choice(available))

        new_packages, new_time = evaluate_solution(
            new_solution, distance_matrix, paczkomaty, speed, max_time
        )

        if new_time <= max_time and (
            new_packages > delivered_packages
            or random.random() < math.exp((new_packages - delivered_packages) / temperature)
        ):
            current_solution = new_solution
            delivered_packages = new_packages
            current_time = new_time

            if delivered_packages > best_packages:
                best_solution = current_solution[:]
                best_packages = delivered_packages
                best_time = current_time

        temperature *= cooling_rate
        if temperature < 1e-8:
            break

    return best_solution, best_packages, best_time