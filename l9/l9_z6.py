# Napisać program, który pobierze od użytkownika zdanie, a następnie policzy występowania
# poszczególnych znaków w danym zdaniu (oprócz znaku spacji), umieści wynik w słowniku i wypisze go
# na ekran. Zastosować metodę .lower(), aby do słownika wprowadzać tylko małe litery niezależnie od
# tego jak zostały wprowadzone przez użytkownika. Litery mają być kluczem, wartością liczba wystąpień.


# Przykład:
# Podaj zdanie: Python jest SUPER!
# {'p': 2, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'j': 1, 'e': 2, 's': 2, 'u': 1, 'r': 1, '!': 1}


# Pobranie zdania od użytkownika
zdanie = input("Podaj zdanie: ")

# Inicjalizacja słownika do przechowywania liczby wystąpień liter
liczba_wystapien = {}

# Przechodzenie przez każdy znak w zdaniu
for znak in zdanie:
    if znak != ' ':  # Ignorowanie spacji
        znak_lower = znak.lower()  # Konwersja znaku na małą literę
        if znak_lower in liczba_wystapien:
            liczba_wystapien[znak_lower] += 1
        else:
            liczba_wystapien[znak_lower] = 1

# Wyświetlenie wyniku
print(liczba_wystapien)
