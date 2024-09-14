# Napisać program, w którym należy sprawdzić we funkcji czy_liczba_doskonala(n), czy podana liczba n jest liczbą doskonała. Funkcja zwraca True jeśli liczba jest liczbą doskonała lub False jeśli nią nie jest. Liczba doskonała to liczba naturalna, która jest sumą wszystkich swych naturalnych dzielników właściwych (to znaczy od niej mniejszych).


# Przykład:
# Podaj licnę którą chcesz sprawdzić:6
# Liczba 6 jest liczbą doskonałą.

# Przykład:
# Podaj licnę którą chcesz sprawdzić:12
# Liczba 12 nie jest liczbą doskonałą.

def czy_liczba_doskonala(n):
    if n <= 1:
        return False
    suma_dzielnikow = sum(i for i in range(1, n) if n % i == 0)
    return suma_dzielnikow == n


liczb = int(input('Podaj licnę którą chcesz sprawdzić:'))
if czy_liczba_doskonala(liczb):
    print(f'Liczba {liczb} jest liczbą doskonałą')
else:
    print(f'Liczba {liczb} nie jest liczbą doskonałą')