import json
import random


def generate_data(filename: str, n: int) -> None:
    grid_size = 100
    max_packages = 10

    data = {
        "baza": [
            random.randint(int(0.3 * grid_size), int(0.7 * grid_size)),
            random.randint(int(0.3 * grid_size), int(0.7 * grid_size)),
        ],
        "paczkomaty": [],
    }

    for i in range(1, n + 1):
        paczkomat = {
            "id": i,
            "x": random.randint(0, grid_size),
            "y": random.randint(0, grid_size),
            "liczba_paczek": random.randint(1, max_packages),
        }
        data["paczkomaty"].append(paczkomat)

    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)