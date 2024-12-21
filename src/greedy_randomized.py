import random


def greedy_randomized(distance_matrix, paczkomaty, alpha=0.2, max_time=8.0, speed=30.0):
    num_paczkomaty = len(paczkomaty)
    visited = [False] * (num_paczkomaty + 1)
    route = [0]
    current_time = 0.0
    delivered_packages = 0
    current_location = 0

    while True:
        candidates = []

        for paczkomat_id in range(1, num_paczkomaty + 1):
            if not visited[paczkomat_id]:
                distance = distance_matrix[current_location][paczkomat_id]
                if distance == 0:
                    continue
                ratio = paczkomaty[paczkomat_id]["liczba_paczek"] / distance
                candidates.append((paczkomat_id, ratio))

        if not candidates:
            break

        candidates.sort(key=lambda x: x[1], reverse=True)
        top_k = max(1, int(len(candidates) * alpha))
        chosen = random.choice(candidates[:top_k])
        best_next = chosen[0]

        time_to_next = distance_matrix[current_location][best_next] / speed
        time_back_to_base = distance_matrix[best_next][0] / speed

        if current_time + time_to_next + time_back_to_base <= max_time:
            current_time += time_to_next
            delivered_packages += paczkomaty[best_next]["liczba_paczek"]
            visited[best_next] = True
            route.append(best_next)
            current_location = best_next
        else:
            break

    current_time += distance_matrix[current_location][0] / speed
    route.append(0)
    return route, delivered_packages, current_time