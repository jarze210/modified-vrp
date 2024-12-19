import json
import math


def read_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_distance(point1: tuple, point2: tuple) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def build_distance_matrix(file_path: str):
    data = read_json(file_path)
    base = tuple(data["baza"])
    paczkomaty = {p["id"]: p for p in data["paczkomaty"]}

    points = [base] + [(p["x"], p["y"]) for p in paczkomaty.values()]
    size = len(points)
    matrix = [[0.0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = calculate_distance(points[i], points[j])

    return matrix, paczkomaty