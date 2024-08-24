# Lista 7 Zad. 5
# Napisać program sprawdzający czy osoba urodzona w danym roku jest pełnoletnia
# Przykład:
# Podaj swoje imię: Marian
# Podaj rok urodzenia: 1833
# Marian, masz 191 lat, jesteś pełnoletni.

from datetime import datetime

# Pobieranie danych od użytkownika
name = input("Podaj swoje imię: ")
year_of_birth = int(input("Podaj rok urodzenia: "))

# Obliczanie wieku
current_year = datetime.now().year
age = current_year - year_of_birth

# Sprawdzenie pełnoletności
if age >= 18:
    print(f"{name}, masz {age} lat, jesteś pełnoletni.")
else:
    print(f"{name}, masz {age} lat, nie jesteś pełnoletni.")
