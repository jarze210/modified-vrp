from itertools import permutations


def bruteforce(distance_matrix, paczkomaty, max_time=8.0, speed=30.0):
    num_paczkomaty = len(paczkomaty)
    best_route = [0, 0]
    max_packages = 0
    best_time = 0.0

    numbers = list(range(1, num_paczkomaty + 1))

    for i in range(1, num_paczkomaty + 1):
        for perm in permutations(numbers, i):
            route = [0] + list(perm) + [0]
            current_time = 0.0
            delivered_packages = 0
            valid = True

            for j in range(1, len(route)):
                distance = distance_matrix[route[j - 1]][route[j]]
                current_time += distance / speed
                if current_time > max_time:
                    valid = False
                    break
                if route[j] != 0:
                    delivered_packages += paczkomaty[route[j]]["liczba_paczek"]

            if valid and delivered_packages > max_packages:
                max_packages = delivered_packages
                best_route = route
                best_time = current_time

    return best_route, max_packages, best_time