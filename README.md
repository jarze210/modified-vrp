English | [Polski](README.pl.md)

# Modified Vehicle Routing Problem (VRP)

A Combinatorial Optimization project comparing five algorithms (exact, heuristic, and metaheuristic) for a modified Vehicle Routing Problem focused on maximizing the number of delivered packages within a fixed time limit.

## Problem Description

A delivery driver departs from a central depot, visits parcel lockers, and must return to the depot within a maximum time of 8 hours (assuming a constant speed of 30 km/h). The objective is to maximize the total number of delivered packages.

* Each parcel locker has coordinates on a $100 \times 100$ km map, a unique ID, and an assigned number of packages (from 1 to 10).
* Parcel lockers have no capacity limit, and the driver carries all required packages for the area.
* Distances between points are calculated as Euclidean (straight-line) distances.
* Depot coordinates are randomly generated within the 30%–70% range of the map dimensions (30 to 70 km) so the base stays near the center.

### Mathematical Model

Objective function: maximize the total number of delivered packages $Y$:

$$Y = \sum_{j=1}^{n} p_j \cdot x_j$$

where:
* $p_j$ is the number of packages assigned to parcel locker $j$,
* $x_j \in \{0, 1\}$ is a decision variable ($x_j = 1$ if locker $j$ is visited, $0$ otherwise),
* subject to the total route duration (depot $\rightarrow$ visited lockers $\rightarrow$ depot) not exceeding 8 hours.

## Implemented Algorithms

All algorithms share a precomputed Euclidean distance matrix (`src/utils.py`) to avoid recalculating distances during execution:

1. Brute Force (`src/bruteforce.py`) – $O(n \cdot n!)$: Checks all possible permutations of all route lengths. Guarantees the optimal solution, but is computationally infeasible beyond $n = 10$.
2. Greedy (`src/greedy.py`) – $O(n^2)$: Always selects the unvisited locker with the highest `packages / distance` ratio. Very fast, no optimality guarantee.
3. Greedy Randomized (`src/greedy_randomized.py`) – $O(n^2 \log n)$: Randomly picks the next locker from the top 20% (`alpha = 0.2`) candidates ranked by `packages / distance`.
4. Nearest Neighbor (`src/nearest_neighbor.py`) – $O(n^2)$: Always moves to the closest unvisited parcel locker as long as there is enough time left to return to the depot.
5. Simulated Annealing (`src/simulated_annealing.py`) – $O(T \cdot n)$: Metaheuristic starting from a random feasible route and iteratively modifying it (swapping, removing, or inserting lockers) over $T = 10\,000$ iterations with cooling rate `0.997`.

## How to Run

```bash
python3 main.py
```

By default, `main.py` generates a sample dataset in `data/` and benchmarks all algorithms for `n = 10` (Brute Force is automatically skipped for `n > 10`).

## Solution Quality Tests

Tests were conducted for two instance sizes: $n = 10$ and $n = 30$. Randomized algorithms were run 5 times on the same dataset, and the best result was recorded.

### Instance $n = 10$

![Map for n=10](docs/images/n=10%20mapa.PNG)

| Algorithm | Best Route | Packages Delivered |
| --- | --- | --- |
| Brute Force | `[0, 2, 5, 10, 8, 4, 6, 9, 7, 3, 0]` | 59 |
| Greedy | `[0, 3, 7, 6, 2, 8, 10, 5, 0]` | 57 |
| Greedy Randomized | `[0, 3, 7, 6, 2, 8, 10, 5, 0]` | 57 |
| Nearest Neighbor | `[0, 2, 8, 10, 5, 3, 7, 4, 6, 9, 0]` | 59 |
| Simulated Annealing | `[0, 3, 2, 8, 10, 5, 7, 6, 4, 0]` | 58 |

#### 1. Brute Force ($n = 10$)
![Brute Force route n=10](docs/images/trasa%20bruteforce%20n-10.PNG)

#### 2. Greedy ($n = 10$)
![Greedy route n=10](docs/images/trasa%20greedy%20n=10.PNG)

#### 3. Greedy Randomized ($n = 10$)
![Greedy Randomized route n=10](docs/images/trasa%20greedy%20randomized%20n%20=%2010.PNG)

#### 4. Nearest Neighbor ($n = 10$)
![Nearest Neighbor route n=10](docs/images/trasa%20somsiad%20n=10.PNG)

#### 5. Simulated Annealing ($n = 10$)
![Simulated Annealing route n=10](docs/images/trasa%20wyzarzanie%20n=10.PNG)

### Instance $n = 30$

Due to its $O(n \cdot n!)$ complexity, Brute Force was excluded from the $n = 30$ test.

![Map for n=30](docs/images/n=30%20mapa.PNG)

| Algorithm | Best Route | Packages Delivered |
| --- | --- | --- |
| Greedy | `[0, 9, 4, 14, 20, 22, 8, 2, 29, 1, 3, 19, 28, 5, 0]` | 97 |
| Greedy Randomized | `[0, 9, 14, 20, 22, 2, 29, 1, 7, 18, 12, 3, 0]` | 81 |
| Nearest Neighbor | `[0, 24, 26, 23, 18, 12, 13, 6, 7, 1, 3, 29, 2, 8, 0]` | 83 |
| Simulated Annealing | `[0, 29, 1, 3, 9, 14, 8, 20, 0]` | 64 |

#### 1. Greedy ($n = 30$)
![Greedy route n=30](docs/images/trasa%20greedy%20n=30.PNG)

#### 2. Greedy Randomized ($n = 30$)
![Greedy Randomized route n=30](docs/images/trasa%20greedy%20randomized%20n=30.PNG)

#### 3. Nearest Neighbor ($n = 30$)
![Nearest Neighbor route n=30](docs/images/trasa%20somsiad%20n=30.PNG)

#### 4. Simulated Annealing ($n = 30$)
![Simulated Annealing route n=30](docs/images/trasa%20wyzarzanie%20n=30.PNG)

## Execution Time Benchmarks

Each algorithm was tested across 10 different input sizes (3 different datasets per size). The charts show the average execution time for each value of $n$.

### 1. Brute Force
![Brute Force execution time](docs/images/czas%20bruteforce.PNG)

### 2. Greedy
![Greedy execution time](docs/images/czas%20greedy.PNG)

### 3. Greedy Randomized
![Greedy Randomized execution time](docs/images/czas%20greedy%20losowy.PNG)

### 4. Nearest Neighbor
![Nearest Neighbor execution time](docs/images/czas%20somsiad.PNG)

### 5. Simulated Annealing
![Simulated Annealing execution time](docs/images/czas%20wyzarzanie.PNG)

## Conclusions

* Brute Force is the only algorithm that guarantees the optimal solution, but its factorial time complexity makes it impractical for $n > 10$.
* Greedy and Greedy Randomized find strong solutions very quickly. Depending on the instance and randomness, either can slightly outperform the other.
* Nearest Neighbor can outperform greedy variants on certain instances because greedy algorithms tend to jump across the map chasing high-ratio lockers, whereas Nearest Neighbor visits more lockers along compact paths.
* Simulated Annealing underperformed on this problem. With $n \cdot n!$ possible routes (over 36.2 million even for $n = 10$), 10,000 iterations were insufficient to consistently reach optimal solutions while taking noticeably longer than the fast heuristics.

## References

* [Vehicle Routing Problem – Wikipedia](https://en.wikipedia.org/wiki/Vehicle_routing_problem)
* [Dantzig, G. B., & Ramser, J. H. (1959). The Truck Dispatching Problem](https://ideas.repec.org/a/inm/ormnsc/v6y1959i1p80-91.html)