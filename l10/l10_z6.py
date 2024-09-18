# Napisz program, który będzie zawierał funkcje do analizy danych. Funkcje, jakie powinny zostać zaimplementowane to:

# srednia_wydajnosc – oblicza średnią wydajność z podanej listy,
# maksymalna_wydajnosc – zwraca maksymalną wydajność z listy,
# minimalna_wydajnosc – zwraca minimalną wydajność z listy,
# odchylenie_standardowe – oblicza odchylenie standardowe z listy.
# Dane wydajności to: [120, 150, 130, 170, 140].

# Program powinien:

# W pierwszej części rozwiązać problem bez korzystania z wbudowanych funkcji,
# W drugiej części zastosować wbudowane funkcje Pythona.
# Oba rozwiązania powinny znajdować się w jednym pliku.
# Wyniki wyświetl na ekranie i porównaj je.

# Tip

# Przykład:
# Obliczenia bez wbudowanych funkcji:
# Średnia wydajność: 142.0
# Maksymalna wydajność: 170
# Minimalna wydajność: 120
# Odchylenie standardowe: 17.204650534085253
# Obliczenia z wbudowanymi funkcjami:
# Średnia wydajność: 142.0
# Maksymalna wydajność: 170
# Minimalna wydajność: 120
# Odchylenie standardowe: 17.204650534085253

import math

# Wydajności
wydajnosci = [120, 150, 130, 170, 140]

# Funkcje bez wbudowanych funkcji
def srednia_wydajnosc(lista):
    suma = 0
    for wydajnosc in lista:
        suma += wydajnosc
    return suma / len(lista)

def maksymalna_wydajnosc(lista):
    maks = lista[0]
    for wydajnosc in lista:
        if wydajnosc > maks:
            maks = wydajnosc
    return maks

def minimalna_wydajnosc(lista):
    min_wydajnosc = lista[0]
    for wydajnosc in lista:
        if wydajnosc < min_wydajnosc:
            min_wydajnosc = wydajnosc
    return min_wydajnosc

def odchylenie_standardowe(lista):
    srednia = srednia_wydajnosc(lista)
    suma_kwadratow = 0
    for wydajnosc in lista:
        suma_kwadratow += (wydajnosc - srednia) ** 2
    return math.sqrt(suma_kwadratow / len(lista))

# Funkcje z wbudowanymi funkcjami
def srednia_wydajnosc_wbudowana(lista):
    return sum(lista) / len(lista)

def maksymalna_wydajnosc_wbudowana(lista):
    return max(lista)

def minimalna_wydajnosc_wbudowana(lista):
    return min(lista)

def odchylenie_standardowe_wbudowana(lista):
    srednia = srednia_wydajnosc_wbudowana(lista)
    suma_kwadratow = sum((wydajnosc - srednia) ** 2 for wydajnosc in lista)
    return math.sqrt(suma_kwadratow / len(lista))

# Wyświetlanie wyników dla funkcji bez wbudowanych funkcji
print("Obliczenia bez wbudowanych funkcji:")
print(f"Średnia wydajność: {srednia_wydajnosc(wydajnosci)}")
print(f"Maksymalna wydajność: {maksymalna_wydajnosc(wydajnosci)}")
print(f"Minimalna wydajność: {minimalna_wydajnosc(wydajnosci)}")
print(f"Odchylenie standardowe: {odchylenie_standardowe(wydajnosci)}")

# Wyświetlanie wyników dla funkcji z wbudowanymi funkcjami
print("\nObliczenia z wbudowanymi funkcjami:")
print(f"Średnia wydajność: {srednia_wydajnosc_wbudowana(wydajnosci)}")
print(f"Maksymalna wydajność: {maksymalna_wydajnosc_wbudowana(wydajnosci)}")
print(f"Minimalna wydajność: {minimalna_wydajnosc_wbudowana(wydajnosci)}")
print(f"Odchylenie standardowe: {odchylenie_standardowe_wbudowana(wydajnosci)}")
