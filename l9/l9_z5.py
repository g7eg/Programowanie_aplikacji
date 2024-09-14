# Przygotować słownik zawierający min 5 kierunków studiów oferowanych na Politechnice Wrocławskiej
# razem z wydziałem, na którym są oferowane. Następnie napisać program, który będzie wskazywał na
# jakim wydziale znajduje się kierunek wyszukiwany przez użytkownika. W przypadku braku takiego
# kierunku poinformuj użytkownika, że nie może studiować tego kierunku na Politechnice Wrocławskiej.


# Przykład:
# Podaj nazwę kierunku studiów: Informatyka
# Kierunek Informatyka znajduje się na Wydział Elektroniki.


# Przykład:
# Podaj nazwę kierunku studiów: Garncarstwo
# Nie możesz studiować kierunku Garncarstwo na Politechnice Wrocławskiej.


# Przygotowanie słownika z kierunkami studiów i wydziałami
kierunki = {
    "Informatyka": "Wydział Elektroniki",
    "Automatyka": "Wydział Elektroniki",
    "Architektura": "Wydział Architektury",
    "Mechanika": "Wydział Mechaniczny",
    "Zarządzanie": "Wydział Zarządzania"
}

# Prośba o wprowadzenie kierunku
kierunek_wyszukiwany = input("Podaj nazwę kierunku studiów: ")

# Sprawdzenie, czy kierunek znajduje się w słowniku i wyświetlenie odpowiedniego komunikatu
if kierunek_wyszukiwany in kierunki:
    print(f"Kierunek {kierunek_wyszukiwany} znajduje się na {kierunki[kierunek_wyszukiwany]}.")
else:
    print(f"Nie możesz studiować kierunku {kierunek_wyszukiwany} na Politechnice Wrocławskiej.")
