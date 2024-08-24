# Lista 7 Zad. 6
# Napisać program, który sprawdzi czy podana liczba jest parzysta i wyświetli odpowiedni komunikat.
# Przykład:
# Podaj liczbę: 34
# Liczba 34 jest parzysta.
# Przykład:
# Podaj liczbę: -123
# Liczba -123 jest nieparzysta.

# Pobieranie liczby od użytkownika
number = int(input("Podaj liczbę: "))

# Sprawdzanie parzystości
if number % 2 == 0:
    print(f"Liczba {number} jest parzysta.")
else:
    print(f"Liczba {number} jest nieparzysta.")
