[English](README.md) | Polski

# Zmodyfikowany Vehicle Routing Problem (Problem Marszrutyzacji)

Projekt z zakresu optymalizacji kombinatorycznej porównujący pięć algorytmów (dokładny, heurystyczne oraz metaheurystyczny) dla zmodyfikowanego problemu marszrutyzacji pojazdów (VRP), którego celem jest maksymalizacja liczby dostarczonych przesyłek w ograniczonym czasie.

## Opis problemu

Kierowca wyjeżdża z bazy, do której musi wrócić, i ma za zadanie dostarczyć jak największą liczbę przesyłek do różnych paczkomatów w czasie nieprzekraczającym 8 godzin (przy stałej prędkości 30 km/h).

* Każdy paczkomat ma współrzędne na mapie o rozmiarze $100 \times 100$ km, swój numer identyfikacyjny oraz liczbę paczek do dostarczenia (od 1 do 10).
* Do jednego paczkomatu może trafić więcej niż jedna paczka, paczkomat nie ma limitu pojemności, a kierowca ma w samochodzie wszystkie możliwe paczki dla danego obszaru.
* Odległość między dwoma punktami obliczana jest jako odległość euklidesowa (w linii prostej).
* Współrzędne bazy są generowane losowo w przedziale 30%–70% wymiarów mapy (od 30 do 70), dzięki czemu baza zawsze znajduje się w okolicach środka.

### Model problemu

Funkcja celu: zmaksymalizować łączną liczbę dostarczonych paczek $Y$:

$$Y = \sum_{j=1}^{n} p_j \cdot x_j$$

gdzie:
* $p_j$ to liczba paczek przypisana do paczkomatu $j$,
* $x_j \in \{0, 1\}$ to zmienna decyzyjna ($x_j = 1$ oznacza, że paczkomat $j$ został odwiedzony, $x_j = 0$ że nie został odwiedzony),
* z ograniczeniem, że łączny czas przejazdu (wyjazd z bazy, odwiedzenie paczkomatów i powrót do bazy) wynosi co najwyżej 8 godzin.

## Zaimplementowane algorytmy

Wszystkie algorytmy korzystają ze wstępnie wyliczonej macierzy odległości (`src/utils.py`), dzięki czemu dystanse nie są przeliczane ponownie w każdej iteracji:

1. Algorytm siłowy (`src/bruteforce.py`) – $O(n \cdot n!)$: Tworzy wszystkie możliwe permutacje dla wszystkich długości ścieżki. Gwarantuje najlepsze rozwiązanie, ale jest bardzo nieefektywny czasowo powyżej $n = 10$.
2. Algorytm zachłanny (`src/greedy.py`) – $O(n^2)$: Wybiera nieodwiedzony paczkomat o najwyższym stosunku `liczba_paczek / distance`. Działa bardzo szybko, ale nie gwarantuje optimum.
3. Algorytm zachłanny ulosowiony (`src/greedy_randomized.py`) – $O(n^2 \log n)$: Wybiera losowo jeden z top 20% (`alpha = 0.2`) najlepszych kandydatów według stosunku `liczba_paczek / distance`.
4. Najbliższy sąsiad (`src/nearest_neighbor.py`) – $O(n^2)$: Zawsze wybiera najbliższy nieodwiedzony paczkomat, dopóki starcza czasu na powrót do bazy.
5. Symulowane wyżarzanie (`src/simulated_annealing.py`) – $O(T \cdot n)$: Metaheurystyka losująca dopuszczalne rozwiązanie początkowe i modyfikująca je (zamiana kolejności, usuwanie, dodawanie paczkomatów) przez $T = 10\,000$ iteracji ze współczynnikiem chłodzenia `0.997`.

## Uruchomienie

```bash
python3 main.py
```

Domyślnie `main.py` generuje przykładowe dane w folderze `data/` i uruchamia testy dla `n = 10` (dla `n > 10` algorytm siłowy jest automatycznie pomijany).

## Testy jakości rozwiązań

Testy zostały przeprowadzone dla dwóch wartości: $n = 10$ oraz $n = 30$. Algorytmy z elementem losowości uruchamiano 5 razy na tym samym zestawie danych, zapisując najlepsze znalezione rozwiązanie.

### Instancja $n = 10$

![Mapa dla n=10](docs/images/n=10%20mapa.PNG)

| Algorytm | Najlepsza trasa | Dostarczone paczki |
| --- | --- | --- |
| Algorytm siłowy | `[0, 2, 5, 10, 8, 4, 6, 9, 7, 3, 0]` | 59 |
| Algorytm zachłanny | `[0, 3, 7, 6, 2, 8, 10, 5, 0]` | 57 |
| Algorytm zachłanny ulosowiony | `[0, 3, 7, 6, 2, 8, 10, 5, 0]` | 57 |
| Najbliższy sąsiad | `[0, 2, 8, 10, 5, 3, 7, 4, 6, 9, 0]` | 59 |
| Symulowane wyżarzanie | `[0, 3, 2, 8, 10, 5, 7, 6, 4, 0]` | 58 |

#### 1. Algorytm siłowy ($n = 10$)
![Trasa algorytmu siłowego n=10](docs/images/trasa%20bruteforce%20n-10.PNG)

#### 2. Algorytm zachłanny ($n = 10$)
![Trasa algorytmu zachłannego n=10](docs/images/trasa%20greedy%20n=10.PNG)

#### 3. Algorytm zachłanny ulosowiony ($n = 10$)
![Trasa algorytmu zachłannego ulosowionego n=10](docs/images/trasa%20greedy%20randomized%20n%20=%2010.PNG)

#### 4. Algorytm najbliższego sąsiada ($n = 10$)
![Trasa algorytmu najbliższego sąsiada n=10](docs/images/trasa%20somsiad%20n=10.PNG)

#### 5. Algorytm wyżarzania ($n = 10$)
![Trasa algorytmu wyżarzania n=10](docs/images/trasa%20wyzarzanie%20n=10.PNG)

### Instancja $n = 30$

Ze względu na złożoność obliczeniową $O(n \cdot n!)$ algorytm siłowy nie został sprawdzony dla $n = 30$.

![Mapa dla n=30](docs/images/n=30%20mapa.PNG)

| Algorytm | Najlepsza trasa | Dostarczone paczki |
| --- | --- | --- |
| Algorytm zachłanny | `[0, 9, 4, 14, 20, 22, 8, 2, 29, 1, 3, 19, 28, 5, 0]` | 97 |
| Algorytm zachłanny ulosowiony | `[0, 9, 14, 20, 22, 2, 29, 1, 7, 18, 12, 3, 0]` | 81 |
| Najbliższy sąsiad | `[0, 24, 26, 23, 18, 12, 13, 6, 7, 1, 3, 29, 2, 8, 0]` | 83 |
| Symulowane wyżarzanie | `[0, 29, 1, 3, 9, 14, 8, 20, 0]` | 64 |

#### 1. Algorytm zachłanny ($n = 30$)
![Trasa algorytmu zachłannego n=30](docs/images/trasa%20greedy%20n=30.PNG)

#### 2. Algorytm zachłanny ulosowiony ($n = 30$)
![Trasa algorytmu zachłannego ulosowionego n=30](docs/images/trasa%20greedy%20randomized%20n=30.PNG)

#### 3. Algorytm najbliższego sąsiada ($n = 30$)
![Trasa algorytmu najbliższego sąsiada n=30](docs/images/trasa%20somsiad%20n=30.PNG)

#### 4. Algorytm wyżarzania ($n = 30$)
![Trasa algorytmu wyżarzania n=30](docs/images/trasa%20wyzarzanie%20n=30.PNG)

## Testy jakości czasowej

Każdy algorytm został przetestowany 3 razy na 3 różnych zestawach danych dla 10 różnych długości instancji. Na wykresach przedstawiono średni czas wykonania dla danej liczby paczkomatów.

### 1. Algorytm siłowy
![Czas wykonania algorytmu siłowego](docs/images/czas%20bruteforce.PNG)

### 2. Algorytm zachłanny
![Czas wykonania algorytmu zachłannego](docs/images/czas%20greedy.PNG)

### 3. Algorytm zachłanny ulosowiony
![Czas wykonania algorytmu zachłannego ulosowionego](docs/images/czas%20greedy%20losowy.PNG)

### 4. Algorytm najbliższego sąsiada
![Czas wykonania algorytmu najbliższego sąsiada](docs/images/czas%20somsiad.PNG)

### 5. Algorytm symulowanego wyżarzania
![Czas wykonania algorytmu symulowanego wyżarzania](docs/images/czas%20wyzarzanie.PNG)

## Wnioski

* Algorytm siłowy jako jedyny gwarantuje optymalne rozwiązanie, jednak jest skrajnie nieefektywny czasowo – powyżej 10 paczkomatów nie jest wart uruchamiania.
* Algorytmy zachłanny oraz zachłanny ulosowiony znajdują dobre rozwiązania w bardzo krótkim czasie; w zależności od instancji i losowości różnice między nimi są niewielkie.
* Algorytm najbliższego sąsiada potrafi znaleźć lepsze rozwiązanie dla większej liczby paczkomatów, ponieważ algorytmy zachłanne „skaczą” po mapie za najbardziej opłacalnymi punktami, podczas gdy najbliższy sąsiad odwiedza więcej paczkomatów po krótszych odcinkach.
* Symulowane wyżarzanie nie sprawdziło się najlepiej w tym problemie. Przy $n \cdot n!$ możliwych tras (dla $n = 10$ to ponad 36,2 mln) 10 000 iteracji nie wystarcza do znalezienia optimum, a jednocześnie trwa zauważalnie dłużej niż szybkie heurystyki, które dają lepsze wyniki.

## Literatura

* [Vehicle Routing Problem – Wikipedia](https://en.wikipedia.org/wiki/Vehicle_routing_problem)
* [Dantzig, G. B., & Ramser, J. H. (1959). The Truck Dispatching Problem](https://ideas.repec.org/a/inm/ormnsc/v6y1959i1p80-91.html)